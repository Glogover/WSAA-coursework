import requests
import json
#from config import config as cfg

filename = "repos-private.json"

url = 'https://api.github.com/repos/Glogover/principles_of_data_analytics'

apikey = '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'

response = requests.get(url, auth = ('token', apikey)) # make the request to the API with authentication using a personal access token

print(response.status_code) 
#print (response.json())

with open(filename, 'w') as fp:
    repoJSON = response.json() # convert the response to JSON format
    json.dump(repoJSON, fp, indent=4) # write the JSON data to a file