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
from typing import Optional, List
from urllib.parse import urljoin

API_BASE = "https://api.github.com"


def get_session(token: Optional[str]):
    s = requests.Session()
    headers = {
        'Accept': 'application/vnd.github.v3+json',
        'User-Agent': 'ku-wiki-contributors-script'
    }
    if token:
        headers['Authorization'] = f'token {token}'
        print(f"Using authenticated GitHub API (token provided)")
    else:
        print(f"Using unauthenticated GitHub API (limited to 60 requests/hour)")
    s.headers.update(headers)
    return s


def paged_get(session: requests.Session, url: str):
    items = []
    page = 1
    while url:
        print(f"Fetching page {page} from {url}")
        try:
            r = session.get(url, timeout=10)
            r.raise_for_status()
        except requests.exceptions.Timeout:
            print(f"Timeout fetching {url}")
            sys.exit(1)
        except requests.exceptions.HTTPError as e:
            print(f"HTTP Error {r.status_code}: {r.text}")
            sys.exit(1)
        except Exception as e:
            print(f"Error fetching {url}: {e}")
            sys.exit(1)
        
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
        page += 1
    
    print(f"Fetched {len(items)} items total")
    return items


def fetch_contributors(session: requests.Session, owner: str, repo: str):
    url = f"{API_BASE}/repos/{owner}/{repo}/contributors?per_page=100"
    print(f"Fetching contributors from {url}")
    return paged_get(session, url)


def fetch_user(session: requests.Session, login: str):
    url = f"{API_BASE}/users/{login}"
    try:
        r = session.get(url, timeout=10)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        print(f"Warning: Failed to fetch user {login}: {e}")
        return None


def main(argv: List[str]):
    p = argparse.ArgumentParser()
    p.add_argument('--owner', required=True)
    p.add_argument('--repo', required=True)
    p.add_argument('--output', default='docs/data/contributors.yml')
    p.add_argument('--full', action='store_true', help='Fetch full user profile (extra API calls)')
    args = p.parse_args(argv)

    print(f"Starting contributors fetch for {args.owner}/{args.repo}")
    
    token = os.environ.get('GITHUB_TOKEN')
    if token:
        print(f"GITHUB_TOKEN is set")
    else:
        print(f"Warning: GITHUB_TOKEN not set, using unauthenticated API")
    
    session = get_session(token)

    print(f"Fetching contributors for {args.owner}/{args.repo} ...")
    try:
        contributors = fetch_contributors(session, args.owner, args.repo)
    except Exception as e:
        print(f"Error fetching contributors: {e}")
        sys.exit(2)

    if not contributors:
        print(f"Warning: No contributors found")

    out = []
    for i, c in enumerate(contributors, 1):
        entry = {
            'login': c.get('login'),
            'html_url': c.get('html_url'),
            'avatar_url': c.get('avatar_url'),
            'contributions': c.get('contributions')
        }
        if args.full and c.get('login'):
            try:
                user = fetch_user(session, c['login'])
                if user:
                    # include name if present
                    if user.get('name'):
                        entry['name'] = user.get('name')
                    if user.get('email'):
                        entry['email'] = user.get('email')
            except Exception as e:
                # ignore failure to fetch user details
                print(f"Failed to fetch full profile for {c['login']}: {e}")
                pass
        
        if i % 10 == 0:
            print(f"Processed {i} contributors")
        out.append(entry)

    # ensure output dir exists
    out_dir = os.path.dirname(args.output)
    if out_dir:
        try:
            os.makedirs(out_dir, exist_ok=True)
            print(f"Output directory ready: {out_dir}")
        except Exception as e:
            print(f"Error creating output directory {out_dir}: {e}")
            sys.exit(1)

    try:
        with open(args.output, 'w', encoding='utf-8') as fh:
            yaml.safe_dump(out, fh, allow_unicode=True, sort_keys=False)
        print(f"Successfully wrote {len(out)} contributors to {args.output}")
    except Exception as e:
        print(f"Error writing output file {args.output}: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main(sys.argv[1:])
