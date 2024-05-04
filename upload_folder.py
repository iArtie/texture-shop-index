from io import BytesIO
import os
import zipfile
import re
import requests

if not os.path.exists("packs/"):
    os.mkdir("packs")

url = re.search(r'(https?://\S+)', os.environ["BODY"]).group(1)
texture_name = re.search(r'### Texture Pack Name\s*(.*?)\s*###', os.environ["BODY"]).group(1)
req = requests.get(url)

with zipfile.ZipFile(BytesIO(req.content)) as zip_ref:
        target_folder = f"packs/{texture_name}"
        if not os.path.exists(target_folder):
            os.mkdir(target_folder)
    
        top_level_dirs = {os.path.split(name)[0] for name in zip_ref.namelist()}

        # If there's only one top-level directory, extract its contents directly
        if len(top_level_dirs) == 1:
            top_level_dir = top_level_dirs.pop()
            for file_info in zip_ref.infolist():
                # Extract only files inside the top-level directory
                if file_info.filename.startswith(top_level_dir) and '/' in file_info.filename[len(top_level_dir):]:
                    zip_ref.extract(file_info, target_folder)
        else:
            zip_ref.extractall(target_folder)
