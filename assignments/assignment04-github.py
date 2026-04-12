# assignment04-github.py
# Author: Marcin Kaminski
# This program replaces "Andrew" with "Marcin" in assignment04-github.txt using GitHub API

import requests # for making API calls
import json # for handling JSON data
from config4 import apikeys as cfg # import API keys from config file
import base64 # for encoding and decoding file content in base64 format required by GitHub API

apiKey = cfg["githubkey"] # get GitHub API key from config file

owner = "Glogover" # GitHub username that owns the repository
repo = "WSAA-coursework" # repository name where the file is located
file = "assignments/assignment04-github.txt" # file path in the repository
branch = "main" # branch name where the file is located

url = f"https://api.github.com/repos/{owner}/{repo}/contents/{file}" # GitHub API endpoint to access the file content, including owner, repo, and file path

headers = { # headers for authentication and content type for GitHub API requests
    "Authorization": f"Bearer {apiKey}", # use Bearer token for authentication with the GitHub API
    "Accept": "application/vnd.github+json" # specify that we want to receive JSON responses from the GitHub API
}

# get file from GitHub
response = requests.get(url, headers=headers, params={"ref": branch}) # API call to get the file content from GitHub, specifying the branch to ensure we get the correct version of the file
response.raise_for_status() # check if the API call was successful, if not it will raise an HTTP error with the status code and error message
data = response.json() # parse the JSON response from the GitHub API to get the file content and metadata, such as the SHA hash needed for updating the file later

# For additional information on the Secure Hash Algorithm (SHA), see: https://en.wikipedia.org/wiki/Secure_Hash_Algorithms

# decode content
content = base64.b64decode(data["content"]).decode("utf-8") # GitHub API returns file content in base64 encoding, so we need to decode it to get the original text content of the file

# replace text if needed
if "Andrew" in content: # check if the string "Andrew" is present in the file content, if it is, we will replace it with "Marcin"
    content = content.replace("Andrew", "Marcin")

    update = { # prepare the data for updating the file on GitHub, including the commit message, the new content encoded in base64 format, the SHA hash of the current file version, and the branch to update
        "message": "Replace Andrew with Marcin", # commit message describing the change being made to the file
        "content": base64.b64encode(content.encode("utf-8")).decode("utf-8"), # encode the updated content back to base64 format as required by the GitHub API for file updates
        "sha": data["sha"], # the SHA hash of the current version of the file, which is required by the GitHub API to ensure we are updating the correct version of the file and to prevent conflicts
        "branch": branch # specify the branch where the file is located to ensure we update the correct version of the file in the repository
    }

    update_response = requests.put(url, headers=headers, json=update) # API call to update the file content on GitHub with the new content, using the PUT method and including the updated data in JSON format
    update_response.raise_for_status() # check if the API call to update the file was successful, if not it will raise an HTTP error with the status code and error message
    print("File updated") # print a message indicating that the file was successfully updated on GitHub

else:
    print("No changes needed") # if the string "Andrew" is not found in the file content, we print a message indicating that no changes were needed and the file remains unchanged

# End of program