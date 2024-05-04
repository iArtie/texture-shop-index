import sys
import requests

author = sys.argv[1]

config = requests.get("https://raw.githubusercontent.com/iArtie/texture-shop-index/main/config.json").json()
print("Yes" if author in config["staff"] else "No")