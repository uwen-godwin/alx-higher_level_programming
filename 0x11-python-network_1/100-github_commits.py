#!/usr/bin/python3

"""
This script takes two arguments: a repository name and an owner name.
It fetches the 10 most recent commits of the specified repository from GitHub
using the GitHub API and prints them in the format <sha>: <author name>.
"""

import sys
import requests


def fetch_commits(repository, owner):
    """
    Fetches the 10 most recent commits of a repository from GitHub.

    Args:
        repository: The name of the repository.
        owner: The owner of the repository.

    Returns:
        A list of dictionaries containing commit information.
    """
    url = f"https://api.github.com/repos/{owner}/{repository}/commits"
    response = requests.get(url)
    return response.json()


def print_commits(commits):
    """
    Prints the 10 most recent commits in the format <sha>: <author name>.

    Args:
        commits: A list of dictionaries containing commit information.
    """
    for commit in commits[:10]:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print(f"{sha}: {author_name}")


if __name__ == "__main__":
    repository_name = sys.argv[1]
    owner_name = sys.argv[2]
    commits = fetch_commits(repository_name, owner_name)
    print_commits(commits)
