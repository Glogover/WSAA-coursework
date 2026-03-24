import requests
import json

#filename = "repos-public.json"
filename = "repos-wsaa-code.json"

url = 'https://api.github.com/repos/andrewbeattycourseware/wsaa-course-material-2024/contents/code' # URL for the GitHub API to get the contents of a specific repository, in this case the 'code' directory of the 'wsaa-course-material-2024' repository.
#url = 'https://api.github.com/users/andrewbeattycourseware/repos?per_page=100' # URL for the GitHub API to get the repositories of a user, with a parameter to get up to 100 repositories per page
#url = 'https://api.github.com/repos/andrewbeattycourseware/apriivateone'

response = requests.get(url) # make the request to the API
print(response.status_code) # check the status code of the response, 200 means success
repoJSON = response.json() # convert the response to JSON format
#print(response.json())

with open(filename, 'w') as fp:
    json.dump(repoJSON, fp, indent=4) # write the JSON data to a file



