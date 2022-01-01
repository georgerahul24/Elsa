import subprocess
import urllib.request
import json
import zipfile
import shutil
import os

current_version = 273
download_path = 'resources/newver.zip'


def updater():
    """This function is used to update the program.
    It uses pip install --upgrade <package> to update the package.
    Then, it connects to the internet and uses git api toget all the release details of Elsa
    then, if the version of Elsa is outdated, it downloads the zipfile and updates the files of Elsa"""
    try:
        print("Starting updater...")
        # Updating packages
        subprocess.Popen("pip install --upgrade magicforelsa", stdout = subprocess.DEVNULL)
        subprocess.Popen("pip install --upgrade task1", stdout = subprocess.DEVNULL)
        subprocess.Popen("pip install --upgrade talk1", stdout = subprocess.DEVNULL)
        # Finding the latest version
        url = "https://api.github.com/repos/georgerahul24/viraver1.1/tags"
        result = json.load(urllib.request.urlopen(url))
        result = tuple(filter(lambda x: x['name'].split(".")[0].lower().startswith("v") is False, result))
        # To be implemented when version 1.2 rolls out
        # latest_version = max([int(i['name'].split(".")[-1]) for i in result if int(i['name'].split(".")[-2]) > 1])
        # download_url = tuple(filter(lambda x: x['name'].split('.')[-1] == str(latest_version) and int(x['name'].split(".")[-2]) > 1, result))[0]['zipball_url']
        latest_version = max(int(i['name'].split(".")[-1]) for i in result)
        download_url = tuple(filter(lambda x: x['name'].split('.')[-1] == str(latest_version), result))[0]['zipball_url']
        if latest_version > current_version:
            # Updating if the current version is outdated
            print("New version available of Elsa is available. It is being installed.Feel Free to carry on!")
            urllib.request.urlretrieve(download_url, download_path)
            with zipfile.ZipFile(download_path, 'r') as zip:
                folder_name = zip.namelist()[0]
                zip.extractall('resources/newversion')
                files_to_copy = ['Elsa.py', 'elsabackend.py', 'updater.py']
                try:
                    os.mkdir('old version')
                except: pass
                for filename in files_to_copy:
                    try:
                        shutil.copy(f'{filename}', f'old version/{filename}')
                        # folder name already contains '/' at the ending so need to add '/' before the filename
                        shutil.copy(f'resources/newversion/{folder_name}{filename}', f'{filename}')
                    except FileNotFoundError:
                        print(f"File {filename} not found in the zip file")
                shutil.rmtree('resources/newversion')
                print("Update complete. Please restart the program to use the new version")
        else:
            print("You are already using the latest version of Elsa")
        print("Closing updater...")
    except Exception as e:
        print(f"Error in updater: {e}")
