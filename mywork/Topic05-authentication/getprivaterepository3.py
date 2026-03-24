import requests
import json
from config2 import apikeys as cfg

filename = "private-repo-full.json"
owner = "Glogover"
repo = "aprivateone"
base_url = f"https://api.github.com/repos/{owner}/{repo}"

apiKey = cfg["githubkey"]

headers = {
    "Authorization": f"token {apiKey}",
    "Accept": "application/vnd.github+json"
}

session = requests.Session()
session.headers.update(headers)


def get_json(url, params=None):
    response = session.get(url, params=params)
    print(f"GET {response.url} -> {response.status_code}")

    if response.status_code != 200:
        return {
            "error": True,
            "status_code": response.status_code,
            "message": response.text
        }

    return response.json()


repo_data = {
    "repository": get_json(base_url),
    "languages": get_json(f"{base_url}/languages"),
    "branches": get_json(f"{base_url}/branches", params={"per_page": 100}),
    "tags": get_json(f"{base_url}/tags", params={"per_page": 100}),
    "contributors": get_json(f"{base_url}/contributors", params={"per_page": 100}),
    "commits": get_json(f"{base_url}/commits", params={"per_page": 30}),
    "releases": get_json(f"{base_url}/releases", params={"per_page": 100}),
    "issues": get_json(f"{base_url}/issues", params={"state": "all", "per_page": 100}),
    "pull_requests": get_json(f"{base_url}/pulls", params={"state": "all", "per_page": 100}),
    "topics": get_json(f"{base_url}/topics"),
    "readme": get_json(f"{base_url}/readme")
}

with open(filename, "w", encoding="utf-8") as fp:
    json.dump(repo_data, fp, indent=4, ensure_ascii=False)

print(f"\nSaved repository data to {filename}")