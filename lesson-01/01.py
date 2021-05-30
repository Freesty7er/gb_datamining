import requests
import json

url = 'https://api.github.com/users/Freesty7er/repos'

response = requests.get(url).json()

repos = []
for i in range(1, len(response)):
    repo = {
        'No' : i,
        'Name' : response[i-1]['name']
    }

    repos.append(repo)

print(repos)

with open('data_repos.json', 'w') as fp:
    json.dump(repos, fp)
