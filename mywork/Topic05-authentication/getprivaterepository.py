import requests
import json

filename = "repos-private.json"

url = 'https://api.github.com/repos/Glogover/principles_of_data_analytics'

# Input your GitHub personal access token here. You can create a personal access token in your GitHub account settings under "Developer settings" -> "Personal access tokens". Make sure to give it the necessary permissions to access private repositories if needed.
apikey = ''

response = requests.get(url, auth = ('token', apikey)) # make the request to the API with authentication using a personal access token

print(response.status_code)
#print (response.json())

with open(filename, 'w') as fp:
    repoJSON = response.json() # convert the response to JSON format
    json.dump(repoJSON, fp, indent=4) # write the JSON data to a file