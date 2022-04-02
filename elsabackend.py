import time

from Magic import chat_client
from Magic import history
from talk1.talk1 import talk
from task1 import task
import os


def quit(event = "") -> None:
    """To exit the program"""
    try: chat_client.closeClient()
    except: pass
    talk("Tata Bye Bye", True)
    exit()


backend1_1_dict = {"bye": (quit, "User exited"), "tata": (quit, "User exited"), "close": (quit, "User exited"), "exit": (quit, "User exited"),
                   "download": (task.download, "Opened downloads folder"),
                   "desktop": (task.desktop, "Opened desktop folder"), "music": (task.musicFolder, "Opened music folder"),
                   "tell jokes": (task.joke, "Told a joke"),
                   "tell a joke": (task.joke, "Told a joke"), "joke": (task.joke, "Told a joke")}


def get_keywords() -> tuple:
    """"To get the list of keywords that are accepted by the backend1_1 function"""
    return tuple(backend1_1_dict.keys())


def backend1_1(order: str) -> None:
    """This function takes the necessary actions according to the input given and then writes
    it to the history file"""
    backend1_1_dict[order][0]()
    history.user_file(order, backend1_1_dict[order][1])


def maintenance_of_files():
    def _compare_and_delete_files(filename):
        file_createdtime = os.path.getmtime(filename)
        currenttime = time.time()
        time_lapse = (currenttime - file_createdtime) / (3600 * 24)  # Getting the number of days since file was modified
        if time_lapse > 3:  # Delete the files if they are greater than 3 days old to re-index them again
            os.remove(filename)

    file_list = ['resources/ indexer.elsa', 'resources/ indexerfolder.elsa']
    for file in file_list:
        _compare_and_delete_files(file)


try:
    maintenance_of_files()
except: pass
