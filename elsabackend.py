from Magic import history
from talk1.talk1 import talk
from task1 import task

backend1_1_dict = {"bye": (quit, "User exited"), "tata": (quit, "User exited"), "close": (quit, "User exited"), "exit": (quit, "User exited"),
                   "time": (task.tell_time, "Told the time"), "download": (task.download, "Opened downloads folder"),
                   "desktop": (task.desktop, "Opened desktop folder"), "music": (task.musicFolder, "Opened music folder"),
                   "tell jokes": (task.joke, "Told a joke"),
                   "tell a joke": (task.joke, "Told a joke"), "joke": (task.joke, "Told a joke")}


def print_talk(pri=None, tal=None):
    print(pri) if pri is not None else 1
    talk(tal) if tal is not None else 1


def quit(event="") -> None:
    """To exit the program"""
    exec("try: chat_client.closeClient()\nexcept:pass")
    print_talk("Tata Bye Bye", "Tata Bye Bye")
    exit()


def get_keywords():
    return tuple(backend1_1_dict.keys())


def backend1_1(order, name):
    backend1_1_dict[order][0]()
    history.user_file(name, order, backend1_1_dict[order][1])
