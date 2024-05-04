from io import BytesIO
import os
import zipfile
import re
import requests

if not os.path.exists("packs/"):
    os.mkdir("packs")

folders_list = []
url = re.search(r'(https?://\S+)', os.environ["BODY"]).group(1)
req = requests.get(url)
# Open the ZIP file
with zipfile.ZipFile(BytesIO(req.content)) as zip_ref:
    # Iterate through files in the ZIP archive
    for file_info in zip_ref.filelist:
        # Extract the filename
        filename = file_info.filename
        # Match folder names using regular expression
        folder_match = re.search(r'.*/$', filename)
        if folder_match:
            # Extract the matched folder name
            folder_name = folder_match.group()
            folders_list.append(folder_name)
    
    try:
        if folders_list[0] != re.match(r"^[^/]+/$", folders_list[0]):
            zip_ref.extractall("packs")
    except IndexError:
        folder = f"packs/{filename.replace('.zip', '')}"
        if not os.path.exists(folder):
            os.mkdir(folder)
        
        zip_ref.extractall(folder)