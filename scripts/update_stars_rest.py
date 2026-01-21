#!/usr/bin/env python3
"""Update GitHub stars using REST API (no gh CLI required).

Reads awesomelist/github_projects.json and updates 'stars' and 'last_updated'.
Requires no external dependencies. Uses GITHUB_TOKEN if available for higher rate limits.
"""

import json
import os
import time
import urllib.request
import urllib.error
from pathlib import Path

DATA_FILE = Path("awesomelist/github_projects.json")


def get_token():
    return os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")


def fetch_repo(repo: str, token: str | None):
    url = f"https://api.github.com/repos/{repo}"
    req = urllib.request.Request(url)
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    req.add_header("Accept", "application/vnd.github+json")
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            if resp.status == 200:
                return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        # rate limit or not found
        return None
    except Exception:
        return None
    return None


def extract_repo(url: str) -> str | None:
    if "github.com/" not in url:
        return None
    repo = url.split("github.com/")[-1].rstrip('/')
    if repo.endswith('.git'):
        repo = repo[:-4]
    # strip tree, issues paths if present
    parts = repo.split('/')
    if len(parts) >= 2:
        return f"{parts[0]}/{parts[1]}"
    return None


def main():
    if not DATA_FILE.exists():
        print("No github_projects.json found")
        return

    token = get_token()
    data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
    updated = 0

    for category in data.get('categories', []):
        for project in category.get('projects', []):
            url = project.get('url', '')
            repo = extract_repo(url)
            if not repo:
                continue
            info = fetch_repo(repo, token)
            if not info:
                continue
            stars = info.get('stargazers_count')
            if stars is None:
                continue
            if project.get('stars') != stars:
                print(f"  {project.get('name','?')}: {project.get('stars','?')} -> {stars}")
                project['stars'] = stars
                project['last_updated'] = time.strftime('%Y-%m-%d')
                updated += 1

    if updated > 0:
        DATA_FILE.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"\nUpdated {updated} projects")
    else:
        print("No updates needed")


if __name__ == '__main__':
    print('Updating GitHub stars via REST API...')
    main()
