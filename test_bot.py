import json
import requests
import os

headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"token {os.environ['TOKEN']}"
}

data = {
    "body": "Accepted texture pack!"
}

closed_data = {
    "state": "closed"
}

requests.post(f"https://api.github.com/repos/iArtie/texture-shop-index/issues/{os.environ['ISSUE_ID']}/comments", headers = headers, json = data)
requests.patch(f"https://api.github.com/repos/iArtie/texture-shop-index/issues/{os.environ['ISSUE_ID']}", headers = headers, json = closed_data)
