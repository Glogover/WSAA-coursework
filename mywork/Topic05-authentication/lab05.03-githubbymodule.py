from github import Github
from config2 import apikeys as cfg

apikey = cfg["githubkey"]

# use your own key
g = Github(apikey)

for repo in g.get_user().get_repos():
    print(repo.name)