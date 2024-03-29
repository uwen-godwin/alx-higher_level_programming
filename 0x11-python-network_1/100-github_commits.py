#!/usr/bin/python3

import requests
import sys

def fetch_commits(repository, owner):
    url = f"https://api.github.com/repos/{owner}/{repository}/commits"
    response = requests.get(url)
    if response.status_code == 200:
        commits = response.json()[:10]
        for commit in commits:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    else:
        print(f"Error: Failed to fetch commits - {response.status_code}")

if __name__ == "__main__":
    repository = sys.argv[1]
    owner = sys.argv[2]
    fetch_commits(repository, owner)
