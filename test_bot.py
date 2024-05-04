import json
import requests
import os

headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {os.environ['TOKEN']}",
    "X-GitHub-Api-Version": "2022-11-28"
}

data = {
    "body": "Accepted texture pack!"
}

req = requests.post(f"https://api.github.com/repos/iArtie/texture-shop-index/issues/{os.environ['ISSUE_ID']}/comments", headers = headers, data = json.dumps(data))

print(req.text)