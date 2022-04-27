import json, socket, threading, os
import tkinter
from functools import partial
from .Elsa_logging import log

from Magic import export_import
from pathlib import Path


def jsonenc(rec, data):
    """To convert the json data"""
    return json.dumps({"rec": rec, "data": data})


def jsondec(data: str) -> dict:
    """To convert the json data"""
    return json.loads(data)


try:
    import win10toast

    noti = win10toast.ToastNotifier()
except ModuleNotFoundError:
    log.error('win10toast module not installed')
host, port = "127.0.0.1", 24094
log.info("Current host: ", host, "Current Port: ", port)
# SOCK_STREAM. AF_INET  -> address-family ipv4 & SOCK_STREAM -> TCP protocol(see geek for geeks)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


class ChatGUI:
    import tkinter
    def __init__(self):
        self.history = chat_handler.get_history()
        self.root = tkinter.Tk()
        self.assests = []
        self.homepage()

    def homepage(self):
        [self.assests.pop().destroy() for _ in range(len(self.assests))]# Removing the elements from list as well as GUI
        for chat_name in self.history:
            b = tkinter.Button(self.root, text = chat_name, command = partial(self.selected_user, chat_name = chat_name))
            b.pack()
            self.assests.append(b)
        self.root.mainloop()

    def selected_user(self, chat_name):
        [self.assests.pop().destroy() for _ in range(len(self.assests))]
        for chats in self.history[chat_name]:
            l = tkinter.Label(self.root, text = chats[1])
            l.pack()
            self.assests.append(l)
        b = tkinter.Button(self.root, text = '<', command = lambda: self.homepage())
        b.pack()
        self.assests.append(b)


class ChatHandler:
    def __init__(self, nickname):
        self.name, self.client, self.file_path = nickname, client, None

    def initialise_history(self):
        """
        This function is to set up user's chat history file
        Note:
        Initialising history using start_client() func inorder to get the username/nickname from Elsa.py
        Else nickname = '' i.e. a blank string instead of the actual name that we want"""
        self.file_path = os.path.join(os.getcwd(), 'chat_data', self.name + '.json')
        if not Path(os.path.join(os.getcwd(), 'chat_data')).exists():  # Creating chat_data folder if it does not exist
            os.mkdir(os.path.join(os.getcwd(), "chat_data"))
            log.info('Created directory', '"chat_data"')
        if not Path(self.file_path).exists():  # Creating the chat file if it does not exist
            with open(self.file_path, 'w') as f:
                json.dump(dict(), f)  # Dumping the empty dictionary to the file
        # TODO: Testing
        ChatGUI()

    def recievefromserver(self) -> None:
        """To receive data from the server"""
        while True:
            client = self.client
            try:
                msg = client.recv(1024).decode("ascii")
                rec = jsondec(msg)["rec"]
                match rec:
                    case "Nick":
                        client.send(jsonenc("Nick", self.name).encode("ascii"))
                    case "msg":
                        sender_name, mesg = jsondec(msg)["data"]
                        print(f"msg received from {sender_name}:", mesg)
                        self.history_write(0, sender_name, mesg)
                        try: noti.show_toast(f"{sender_name}", mesg)
                        except Exception as e: print(e)
                    case "sync":
                        log.info("Starting to sync from the server")
                        export_import.import_data(jsondec(msg)["data"])
                        log.info('Finished syncing data from Server.')

            except Exception as e:
                log.error("Closing Connection", e)
                client.close()
                del client
                break

    def history_write(self, statuscode, client_name, msg):
        """This function is to write the msg to a file.
        statuscode = 0 if user receiving msg
        statuscode = 1 if user is sending the msg
        client_name: from which client the msg is received from or  send to"""
        with open(self.file_path, 'r') as f:
            chat_dict = json.load(f)
            history = chat_dict.get(client_name, [])  # Getting history of the 'client_name' person
            history.append((statuscode, msg))  # Since list is mutable, it will change in the dictionary too.
            chat_dict[client_name] = history
        with open(self.file_path, 'w') as f:
            json.dump(chat_dict, f)

    def get_history(self):
        with open(self.file_path, 'r') as f:
            return json.load(f)

    def sendtoserver(self, reciever_name: str, msg: str) -> None:
        """To send the data to the server"""
        try:
            self.history_write(1, reciever_name, msg)
            client.send(jsonenc("msg", (reciever_name, msg)).encode("ascii"))
            print("Sending", msg, "to", reciever_name)

        except Exception as e:
            log.error(e)

    def sendThemeToServer(self) -> None:
        """To send the theme to the server"""
        data = (self.name, export_import.export(mode = 's'))
        client.send(jsonenc("fsync", data).encode("ascii"))
        log.info('Trying to sync with server')

    def requestSync(self) -> None:
        """To request the file of the user from the server"""
        client.send(jsonenc("sync", self.name).encode("ascii"))
        log.info('Trying to get the file from server')

    def startclient(self) -> None:
        """To start the process of connecting the client with server"""
        try:
            client.connect((host, port))
            self.initialise_history()
            threading.Thread(target = self.recievefromserver).start()
        except ConnectionRefusedError:
            log.error('Could not connect to a server')

    def closeClient(self) -> None:
        """To close the connection of the client with the server"""
        client.close()
        log.info('Closing Client')


chat_handler = ChatHandler("")
