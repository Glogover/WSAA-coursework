import requests # for making HTTP requests to the GitHub API
import json # for working with JSON data, which is the format used by the GitHub API to send and receive data
import base64 # for encoding file content to base64. Base64 is a binary-to-text encoding scheme that represents binary data in an ASCII string format. It is commonly used to encode binary data, such as file contents, into a format that can be easily transmitted over text-based protocols like HTTP.
from config2 import apikeys as cfg

filename = "change-repo.json" # The name of the file where the response from the GitHub API will be saved. This file will contain the JSON response from the API after attempting to create or update a file in the repository.

owner = "Glogover"
repo = "aprivateone"
file_path = "hello.txt"

url = f"https://api.github.com/repos/{owner}/{repo}/contents/{file_path}"

apiKey = cfg['githubkey'] # The GitHub personal access token used for authentication when making requests to the GitHub API. This token should have the necessary permissions to access and modify the repository in question. It is retrieved from a configuration file (config2) where it is stored under the key 'githubkey'.

headers = {
    "Authorization": f"token {apiKey}" # The Authorization header is set to include the personal access token for authentication. The format is "token <your_token>", which is required by the GitHub API to authenticate the request and allow access to private repositories or perform actions that require authentication.
}

# file content to upload
content = "Hello everyone! This is a new file created using the GitHub API."

# encode file content
encoded = base64.b64encode(content.encode()).decode() # encode the content to base64 format. The content is first encoded to bytes using .encode(), then encoded to base64 using base64.b64encode(), and finally decoded back to a string using .decode() for inclusion in the JSON payload sent to the GitHub API.

data = {
    "message": "Add hello.txt using API",
    "content": encoded
}

response = requests.put(url, headers=headers, json=data) # make a PUT request to the GitHub API to create or update the file at the specified path in the repository. The request includes the URL, headers for authentication, and a JSON payload containing the commit message and the base64-encoded content of the file.

print(response.status_code) # Print the HTTP status code of the response. A status code of 201 indicates that the file was successfully created, while a status code of 200 indicates that the file was successfully updated. Other status codes may indicate errors or issues with the request.

result = response.json() # Convert the response from the GitHub API to JSON format. This will contain information about the created or updated file, such as its name, path, SHA, and other metadata. If there was an error with the request, the JSON response may contain error messages or details about what went wrong.

with open(filename, "w") as fp: # Open the specified file in write mode. This file will be used to save the JSON response from the GitHub API after attempting to create or update the file in the repository.
    json.dump(result, fp, indent=4) # Write the JSON response to the file with indentation for better readability. This allows you to review the details of the created or updated file, or any error messages returned by the API, by opening the "change-repo.json" file after running the script.