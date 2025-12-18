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
  --full           Fetch full user profile for each contributor

Authentication:
  Set GITHUB_TOKEN environment variable to increase rate limits.
"""

import argparse
import logging
import os
import sys
from typing import List, Optional

import requests
import yaml

# Constants
API_BASE = "https://api.github.com"
DEFAULT_OUTPUT = "docs/data/contributors.yml"
PER_PAGE = 100
REQUEST_TIMEOUT = 10
PROGRESS_INTERVAL = 10

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)
logger = logging.getLogger(__name__)


def get_session(token: Optional[str]) -> requests.Session:
    """Create a configured requests session."""
    session = requests.Session()
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "ku-wiki-contributors-script",
    }
    if token:
        headers["Authorization"] = f"token {token}"
        logger.info("Using authenticated GitHub API")
    else:
        logger.warning("Using unauthenticated API (60 requests/hour limit)")
    session.headers.update(headers)
    return session


def paged_get(session: requests.Session, url: str) -> List[dict]:
    """Fetch all pages from a paginated GitHub API endpoint."""
    items = []
    page = 1

    while url:
        logger.debug(f"Fetching page {page}: {url}")
        try:
            response = session.get(url, timeout=REQUEST_TIMEOUT)
            response.raise_for_status()
        except requests.exceptions.Timeout:
            logger.error(f"Request timeout: {url}")
            sys.exit(1)
        except requests.exceptions.HTTPError as e:
            logger.error(f"HTTP {response.status_code}: {response.text}")
            sys.exit(1)
        except requests.exceptions.RequestException as e:
            logger.error(f"Request failed: {e}")
            sys.exit(1)

        items.extend(response.json())

        # Parse Link header for pagination
        url = parse_next_link(response.headers.get("Link", ""))
        page += 1

    logger.info(f"Fetched {len(items)} items")
    return items


def parse_next_link(link_header: str) -> Optional[str]:
    """Extract next page URL from Link header."""
    if 'rel="next"' not in link_header:
        return None

    for part in link_header.split(","):
        if 'rel="next"' in part:
            url_part = part.split(";")[0].strip()
            if url_part.startswith("<") and url_part.endswith(">"):
                return url_part[1:-1]
    return None


def fetch_contributors(session: requests.Session, owner: str, repo: str) -> List[dict]:
    """Fetch all contributors for a repository."""
    url = f"{API_BASE}/repos/{owner}/{repo}/contributors?per_page={PER_PAGE}"
    logger.info(f"Fetching contributors for {owner}/{repo}")
    return paged_get(session, url)


def fetch_user(session: requests.Session, login: str) -> Optional[dict]:
    """Fetch detailed user profile."""
    url = f"{API_BASE}/users/{login}"
    try:
        response = session.get(url, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.warning(f"Failed to fetch user {login}: {e}")
        return None


def process_contributors(
    session: requests.Session,
    contributors: List[dict],
    fetch_full: bool
) -> List[dict]:
    """Process contributor data into output format."""
    output = []

    for i, contributor in enumerate(contributors, 1):
        entry = {
            "login": contributor.get("login"),
            "html_url": contributor.get("html_url"),
            "avatar_url": contributor.get("avatar_url"),
            "contributions": contributor.get("contributions"),
        }

        if fetch_full and contributor.get("login"):
            user = fetch_user(session, contributor["login"])
            if user:
                if user.get("name"):
                    entry["name"] = user["name"]
                if user.get("email"):
                    entry["email"] = user["email"]

        if i % PROGRESS_INTERVAL == 0:
            logger.info(f"Processed {i}/{len(contributors)} contributors")

        output.append(entry)

    return output


def write_output(data: List[dict], output_path: str) -> None:
    """Write contributor data to YAML file."""
    output_dir = os.path.dirname(output_path)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        yaml.safe_dump(data, f, allow_unicode=True, sort_keys=False)

    logger.info(f"Wrote {len(data)} contributors to {output_path}")


def main(argv: List[str]) -> None:
    """Main entry point."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--owner", required=True, help="GitHub repo owner")
    parser.add_argument("--repo", required=True, help="GitHub repo name")
    parser.add_argument("--output", default=DEFAULT_OUTPUT, help="Output path")
    parser.add_argument("--full", action="store_true", help="Fetch full profiles")
    parser.add_argument("--debug", action="store_true", help="Enable debug logging")
    args = parser.parse_args(argv)

    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)

    token = os.environ.get("GITHUB_TOKEN")
    session = get_session(token)

    try:
        contributors = fetch_contributors(session, args.owner, args.repo)
    except Exception as e:
        logger.error(f"Failed to fetch contributors: {e}")
        sys.exit(2)

    if not contributors:
        logger.warning("No contributors found")

    output = process_contributors(session, contributors, args.full)
    write_output(output, args.output)


if __name__ == "__main__":
    main(sys.argv[1:])
