import sys
import json

author = sys.argv[1]

config = json.load(open("config.json", "r"))
print("Yes" if author in config["staff"] else "No")
