generate_contributors.py

This script fetches the GitHub contributors list for a repository and writes a YAML file suitable for use by the site.

Usage example:

```bash
# set GitHub token to avoid strict rate limits (optional but recommended)
export GITHUB_TOKEN=ghp_012345...yourtoken...

# from repository root
python3 scripts/generate_contributors.py --owner minamotooRin --repo KU-WIKI \
  --output docs/data/contributors.yml

# to also fetch full user profile (display name / email when public):
python3 scripts/generate_contributors.py --owner minamotooRin --repo KU-WIKI --full
```

Notes:
- The script uses the GitHub REST API and respects pagination.
- If you don't provide a token via `GITHUB_TOKEN`, the script will still work but may be subject to stricter rate limits (60 req/hr).
- The script writes a YAML list of contributors with fields: login, html_url, avatar_url, contributions, and optionally name/email.
