import requests
import sys

def fetch_commits(repository, owner):
    url = f"https://api.github.com/repos/{owner}/{repository}/commits"
    response = requests.get(url)
    if response.status_code == 200:
        commits = response.json()
        for commit in commits[:10]:  # Limit to 10 commits
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    else:
        print("Error:", response.status_code)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 100-github_commits.py <repository_name> <owner_name>")
        sys.exit(1)

    repository_name = sys.argv[1]
    owner_name = sys.argv[2]

    fetch_commits(repository_name, owner_name)
