#!/usr/bin/env python3
"""
Generate docs/data/contributors.yml from GitHub repository contributors.

Usage:
    python3 scripts/generate_contributors.py --owner <owner> --repo <repo> \
        [--output docs/data/contributors.yml] [--full]

Options:
  --owner OWNER    GitHub repo owner (user or org)
  --repo REPO      GitHub repository name
  --output PATH    Output YAML path (default: docs/data/contributors.yml)
  --full           Fetch full user profile (name, email if public) for each contributor (one API call per user)

Authentication:
  To increase rate limits, set environment variable GITHUB_TOKEN with a personal access token.

This script handles GitHub pagination and writes a YAML list of contributors with fields:
  - login
  - name (if available or if --full)
  - html_url
  - avatar_url
  - contributions

"""
import os
import sys
import argparse
import requests
import yaml
from urllib.parse import urljoin

API_BASE = "https://api.github.com"


def get_session(token: str | None):
    s = requests.Session()
    headers = {
        'Accept': 'application/vnd.github.v3+json',
        'User-Agent': 'ku-wiki-contributors-script'
    }
    if token:
        headers['Authorization'] = f'token {token}'
    s.headers.update(headers)
    return s


def paged_get(session: requests.Session, url: str):
    items = []
    while url:
        r = session.get(url)
        r.raise_for_status()
        items.extend(r.json())
        # parse Link header for next
        link = r.headers.get('Link', '')
        next_url = None
        if 'rel="next"' in link:
            parts = link.split(',')
            for p in parts:
                if 'rel="next"' in p:
                    # format: <url>; rel="next"
                    urlpart = p.split(';')[0].strip()
                    if urlpart.startswith('<') and urlpart.endswith('>'):
                        next_url = urlpart[1:-1]
        url = next_url
    return items


def fetch_contributors(session: requests.Session, owner: str, repo: str):
    url = f"{API_BASE}/repos/{owner}/{repo}/contributors?per_page=100"
    return paged_get(session, url)


def fetch_user(session: requests.Session, login: str):
    url = f"{API_BASE}/users/{login}"
    r = session.get(url)
    r.raise_for_status()
    return r.json()


def main(argv: list[str]):
    p = argparse.ArgumentParser()
    p.add_argument('--owner', required=True)
    p.add_argument('--repo', required=True)
    p.add_argument('--output', default='docs/data/contributors.yml')
    p.add_argument('--full', action='store_true', help='Fetch full user profile (extra API calls)')
    args = p.parse_args(argv)

    token = os.environ.get('GITHUB_TOKEN')
    session = get_session(token)

    print(f"Fetching contributors for {args.owner}/{args.repo} ...")
    try:
        contributors = fetch_contributors(session, args.owner, args.repo)
    except requests.HTTPError as e:
        print(f"Error fetching contributors: {e}")
        sys.exit(2)

    out = []
    for c in contributors:
        entry = {
            'login': c.get('login'),
            'html_url': c.get('html_url'),
            'avatar_url': c.get('avatar_url'),
            'contributions': c.get('contributions')
        }
        if args.full and c.get('login'):
            try:
                user = fetch_user(session, c['login'])
                # include name if present
                if user.get('name'):
                    entry['name'] = user.get('name')
                if user.get('email'):
                    entry['email'] = user.get('email')
            except requests.HTTPError:
                # ignore failure to fetch user details
                pass
        out.append(entry)

    # ensure output dir exists
    out_dir = os.path.dirname(args.output)
    if out_dir and not os.path.exists(out_dir):
        os.makedirs(out_dir, exist_ok=True)

    with open(args.output, 'w', encoding='utf-8') as fh:
        yaml.safe_dump(out, fh, allow_unicode=True, sort_keys=False)

    print(f"Wrote {len(out)} contributors to {args.output}")


if __name__ == '__main__':
    main(sys.argv[1:])
