import subprocess
import urllib.request
import json
import zipfile
import shutil
current_version = 272
download_path='resources/newver.zip'

def updater():
    print("Starting updater...")
    subprocess.Popen("pip install --upgrade magicforelsa", stdout = subprocess.DEVNULL)
    subprocess.Popen("pip install --upgrade task1", stdout = subprocess.DEVNULL)
    subprocess.Popen("pip install --upgrade talk1", stdout = subprocess.DEVNULL)
    print("Closing updater...")


url = "https://api.github.com/repos/georgerahul24/viraver1.1/tags"
result = json.load(urllib.request.urlopen(url))
result = tuple(filter(lambda x: x['name'].split(".")[0].lower().startswith("v") is False, result))
# To be implemented when version 1.2 rolls out
# latest_version = max([int(i['name'].split(".")[-1]) for i in result if int(i['name'].split(".")[-2]) > 1])
# download_url = tuple(filter(lambda x: x['name'].split('.')[-1] == str(latest_version) and int(x['name'].split(".")[-2]) > 1, result))[0]['zipball_url']
latest_version = max([int(i['name'].split(".")[-1]) for i in result])
download_url = tuple(filter(lambda x: x['name'].split('.')[-1] == str(latest_version), result))[0]['zipball_url']
if latest_version > current_version:
    print("New version available of Elsa is available. It is being installed.Feel Free to carry on!")
    urllib.request.urlretrieve(download_url, download_path)
    with zipfile.ZipFile(download_path, 'r') as zip:
        foldername = zip.namelist()[0]
        zip.extractall('resources/newversion')
        filestocopy = ['Elsa.py', 'elsabackend.py','updater.py']
        # foldername aldready contains '/' at the ending so need to add '/' before the filename
        for filename in filestocopy:
            try:
                shutil.copy(f'resources/newversion/{foldername}{filename}', f'{filename}')
            except FileNotFoundError:
                print(f"File {filename} not found in the zip file")
        shutil.rmtree('resources/newversion')



