import requests
import json

filename = "repos-private.json"

url = 'https://api.github.com/repos/Glogover/principles_of_data_analytics'

# Before running this code, uncomment the following line
apikey = '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'

# Before running this code, uncomment the following line and replace 'your_personal_access_token' with actual GitHub personal access token
response = requests.get(url, auth = ('token', apikey)) # make the request to the API with authentication using a personal access token

print(response.status_code)
#print (response.json())

with open(filename, 'w') as fp:
    repoJSON = response.json() # convert the response to JSON format
    json.dump(repoJSON, fp, indent=4) # write the JSON data to a file