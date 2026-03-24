import requests
import json

flename = "repos-public.json"

url = 'https://api.github.com/users/andrewbeattycourseware/repos'
#url = 'https://api.github.com/repos/andrewbeattycourseware/apriivateone'

response = requests.get(url) # make the request to the API
print(response.status_code) # check the status code of the response, 200 means success
repoJSON = response.json() # convert the response to JSON format
#print(response.json())

with open(flename, 'w') as fp:
    json.dump(repoJSON, fp, indent=4) # write the JSON data to a file



