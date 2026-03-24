import requests
import json
from config2 import apikeys as cfg

filename = "private-repo.json"

url = 'https://api.github.com/repos/Glogover/aprivateone' # URL for the GitHub API endpoint to get information about a specific repository. Replace 'Glogover/aprivateone' with the owner and repository name you want to access.

# Input your GitHub personal access token here. You can create a personal access token in your GitHub account settings under "Developer settings" -> "Personal access tokens". Make sure to give it the necessary permissions to access private repositories if needed.
apiKey = cfg['githubkey']

response = requests.get(url, auth = ('token', apiKey)) # make the request to the API with authentication using a personal access token

print(response.status_code)
#print (response.json())

repoJSON = response.json() # convert the response to JSON format

with open(filename, 'w') as fp:
    
    json.dump(repoJSON, fp, indent=4) # write the JSON data to a file