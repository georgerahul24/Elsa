from Magic import chat_client
from Magic import history
from talk1.talk1 import talk
from task1 import task

backend1_1_dict = {"bye": (quit, "User exited"), "tata": (quit, "User exited"), "close": (quit, "User exited"), "exit": (quit, "User exited"),
                   "time": (task.tell_time, "Told the time"), "download": (task.download, "Opened downloads folder"),
                   "desktop": (task.desktop, "Opened desktop folder"), "music": (task.musicFolder, "Opened music folder"),
                   "tell jokes": (task.joke, "Told a joke"),
                   "tell a joke": (task.joke, "Told a joke"), "joke": (task.joke, "Told a joke")}


def print_talk(pri: str = None, tal: str = None) -> None:
    """To print aas well as talk the necessary input"""
    print(pri) if pri is not None else None
    talk(tal) if tal is not None else None


def quit(event="") -> None:
    """To exit the program"""
    try: chat_client.closeClient()
    except: pass
    print_talk("Tata Bye Bye", "Tata Bye Bye")
    exit()


def get_keywords() -> tuple:
    """"To get the list of keywords that are accepted by the backend1_1 function"""
    return tuple(backend1_1_dict.keys())


def backend1_1(order: str, name: str) -> None:
    """This function takes the necessary actions according to the input given and then writes
    it to the history file"""
    backend1_1_dict[order][0]()
    history.user_file(name, order, backend1_1_dict[order][1])
