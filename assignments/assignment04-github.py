# assignment04-github.py
# Author: Marcin Kaminski
# This program replaces "Andrew" with "Marcin" in assignment04-github.txt using GitHub API

import requests # for making API calls
import json # for handling JSON data
from config4 import apikeys as cfg # import API keys from config file
import base64 # for encoding and decoding file content in base64 format required by GitHub API

apiKey = cfg["githubkey"] # get GitHub API key from config file

owner = "Glogover"
repo = "WSAA-coursework"
file = "assignments/assignment04-github.txt"
branch = "main"

url = f"https://api.github.com/repos/{owner}/{repo}/contents/{file}"

headers = {
    "Authorization": f"Bearer {apiKey}",
    "Accept": "application/vnd.github+json"
}

# get file from GitHub
response = requests.get(url, headers=headers, params={"ref": branch})
response.raise_for_status()
data = response.json()

# decode content
content = base64.b64decode(data["content"]).decode("utf-8")

# replace text if needed
if "Andrew" in content:
    content = content.replace("Andrew", "Marcin")

    update = {
        "message": "Replace Andrew with Marcin",
        "content": base64.b64encode(content.encode("utf-8")).decode("utf-8"),
        "sha": data["sha"],
        "branch": branch
    }

    update_response = requests.put(url, headers=headers, json=update)
    update_response.raise_for_status()
    print("File updated")

else:
    print("No changes needed")

# End of program