import subprocess, json, zipfile, shutil, os
import urllib.request
from Magic.Elsa_logging import log

current_version = 286
download_path = 'resources/newver.zip'
log.info("Current Elsa version: ", str(current_version))


def updater() -> None:
    """This function is used to update the program.
    It uses pip install --upgrade <package> to update the package.
    Then, it connects to the internet and uses git api toget all the release details of Elsa
    then, if the version of Elsa is outdated, it downloads the zipfile and updates the files of Elsa"""
    try:
        print("Starting updater...")
        # Updating packages
        subprocess.Popen("pip install --upgrade magicforelsa", stdout = subprocess.DEVNULL)
        subprocess.Popen("pip install --upgrade task1", stdout = subprocess.DEVNULL)
        # Finding the latest version
        log.info("Updated libraries from pip")
        url = "https://api.github.com/repos/georgerahul24/viraver1.1/tags"
        log.info("Using url: ", url, " to check for latest version")
        result = json.load(urllib.request.urlopen(url))
        result = tuple(filter(lambda x: x['name'].split(".")[0].lower().startswith("v") is False, result))
        # To be implemented when version 1.2 rolls out
        # latest_version = max([int(i['name'].split(".")[-1]) for i in result if int(i['name'].split(".")[-2]) > 1])
        # download_url = tuple(filter(lambda x: x['name'].split('.')[-1] == str(latest_version) and int(x['name'].split(".")[-2]) > 1, result))[0]['zipball_url']
        latest_version = max(int(i['name'].split(".")[-1]) for i in result)
        download_url = tuple(filter(lambda x: x['name'].split('.')[-1] == str(latest_version), result))[0]['zipball_url']
        log.info('Latest version found as: ', str(latest_version), "Download url for latest version: ", download_url)
        if latest_version > current_version:
            # Updating if the current version is outdated
            log.info("Updating Elsa since newer version has been found")
            print("New version available of Elsa is available. It is being installed.Feel Free to carry on!")
            urllib.request.urlretrieve(download_url, download_path)
            with zipfile.ZipFile(download_path, 'r') as zip:
                folder_name = zip.namelist()[0]
                zip.extractall('resources/newversion')
                files_to_copy = ['Elsa.py', 'elsabackend.py', 'updater.py']
                try:
                    os.mkdir('old version')
                    log.info('Finished backing up files')
                except: pass
                for filename in files_to_copy:
                    try:
                        shutil.copy(f'{filename}', f'old version/{filename}')
                        # folder name already contains '/' at the ending so need to add '/' before the filename
                        shutil.copy(f'resources/newversion/{folder_name}{filename}', f'{filename}')
                        log.info('Copied the latest version of',filename)
                    except FileNotFoundError:
                        print(f"File {filename} not found in the zip file")
                        log.error(f"File {filename} not found in the zip file")
                shutil.rmtree('resources/newversion')
                log.info("Cleaned up resources/newversion folder")
                log.info("Update complete. Please restart the program to use the new version")
        else:
            print("You are already using the latest version of Elsa")
            log.info('Elsa is in the latest version')
        print("Closing updater...")
    except Exception as e:
        log.error(f"Error in updater: {e}")



if __name__ == "__main__": updater()
