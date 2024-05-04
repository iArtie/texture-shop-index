from io import BytesIO
import os
import zipfile
import re
import requests

folders_list = []
url = re.search(r'\((.*?)\)', os.environ["BODY"])
print(os.environ["BODY"])
req = requests.get("https://download1530.mediafire.com/1bx3q8togpzgLBNwddvUGAN_C55mKAcf9Fi7pWVGSfmM_VHOLPDOnUUYuxzsfIGFjr0mA4979H8JD694ot8SKZQQWwZZ9hausHLSD-ErivyxuzmIa3XAk2aEnmCd6ulQkE4a0-dD4ZpROih_FFwUDs0IWn5z6D_fKh1Fkrbp91o/5673zhc0deidsgp/METAL.zip")
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
            zip_ref.extractall()
    except IndexError:
        folder = filename.replace(".zip", "")
        if not os.path.exists(folder):
            os.mkdir(folder)
        
        zip_ref.extractall(folder)
