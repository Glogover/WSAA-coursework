from github import Github
import requests
from config2 import apikeys as cfg

apikey = cfg["githubkey"]

# use your own key
g = Github(apikey)

repo = g.get_repo("Glogover/aprivateone")
#print(repo.clone_url)

fileInfo = repo.get_contents("test.txt")
urlOfFile = fileInfo.download_url
#print (urlOfFile)

#for repo in g.get_user().get_repos():
    #print(repo.name)

response = requests.get(urlOfFile)
contentOfFile = response.text
print (contentOfFile)

newContents = contentOfFile + " more stuff \n"
print (newContents)

gitHubResponse=repo.update_file(fileInfo.path,"updated by prog",
newContents,fileInfo.sha)
print (gitHubResponse)



