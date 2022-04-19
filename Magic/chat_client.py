import json, socket, threading, os
from Magic import export_import
from pathlib import Path


# TODO: incorporate all the isolated functions into a class
def jsonenc(rec, data):
    """To convert the json data"""
    return json.dumps({"rec": rec, "data": data})


def jsondec(data: str) -> dict:
    """To convert the json data"""
    return json.loads(data)


try:
    import win10toast

    noti = win10toast.ToastNotifier()
except ModuleNotFoundError: print("It would be great if win10toast module can be installed")
host, port = "127.0.0.1", 24094
# SOCK_STREAM. AF_INET  -> address-family ipv4 & SOCK_STREAM -> TCP protocol(see geek for geeks)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


class ChatHandler:
    def __init__(self, nickname):
        self.name, self.client = nickname, client

    def initialise_history(self):
        """
        This function is to set up user's chat history file
        Note:
        Initialising history using start_client() func inorder to get the username/nickname from Elsa.py
        Else nickname = '' i.e. a blank string instead of the actual name that we want"""
        self.file_path = os.path.join(os.getcwd(), 'chat_data', self.name + '.json')
        if not Path(os.path.join(os.getcwd(), 'chat_data')).exists():  # Creating chat_data folder if it does not exist
            os.mkdir(os.path.join(os.getcwd(), "chat_data"))
        if not Path(self.file_path).exists():  # Creating the chat file if it does not exist
            with open(self.file_path, 'w') as f:
                json.dump(dict(), f)  # Dumping the empty dictionary to the file

    def jsonenc(self, rec, data):
        """To convert the json data"""
        return json.dumps({"rec": rec, "data": data})

    def jsondec(self, data: str) -> dict:
        """To convert the json data"""
        return json.loads(data)

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
                        print("Starting to sync from the server")
                        export_import.import_data(jsondec(msg)["data"])

            except Exception as e:
                print("Closing Connection", e)
                client.close()
                del client
                break

    def history_write(self, statuscode, client_name, msg):
        """This function is to write the msg to a file.
        statuscode = 0 if user receiving msg
        statuscode = 1 if user is sending the msg
        client_name: from which client the msg is received from or  send to"""
        with open(self.file_path, 'r+') as f:
            chat_dict = json.load(f)
            history = chat_dict.get(client_name, [])  # Getting history of the 'client_name' person
            history.append((statuscode, msg))  # Since list is mutable, it will change in the dictionary too.
            chat_dict[client_name] = history
        with open(self.file_path, 'w') as f:
            json.dump(chat_dict, f)

    def sendtoserver(self, reciever_name: str, msg: str) -> None:
        """To send the data to the server"""
        try:
            self.history_write(1, reciever_name, msg)
            client.send(jsonenc("msg", (reciever_name, msg)).encode("ascii"))
            print("Sending", msg, "to", reciever_name)

        except Exception as e: print(e)

    def sendThemeToServer(self) -> None:
        """To send the theme to the server"""
        data = (self.name, export_import.export(mode = 's'))
        client.send(jsonenc("fsync", data).encode("ascii"))
        print('Trying to sync with server')

    def requestSync(self) -> None:
        """To request the file of the user from the server"""
        client.send(jsonenc("sync", self.name).encode("ascii"))
        print('Trying to get the file from server')

    def startclient(self) -> None:
        """To start the process of connecting the client with server"""
        client.connect((host, port))
        self.initialise_history()
        threading.Thread(target = self.recievefromserver).start()

    def closeClient(self) -> None:
        """To close the connection of the client with the server"""
        client.close()


chat_handler = ChatHandler("")
