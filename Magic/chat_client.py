import json, socket, threading, os
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
except ModuleNotFoundError: print("It would be great if win10toast module can be installed")
host, port, nickname, chat_handler = "127.0.0.1", 24094, "", None
# SOCK_STREAM. AF_INET  -> address-family ipv4 & SOCK_STREAM -> TCP protocol(see geek for geeks)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def getNickname(name: str) -> None:
    """To get the nickname i.e the username of the client"""
    global nickname
    nickname = name


class ChatHandler:
    def __init__(self, nickname):
        self.name = nickname

        self.file_path = os.path.join(os.getcwd(), 'chat_data', nickname + '.json')
        if not Path(os.path.join(os.getcwd(), 'chat_data')).exists():  # Creating chat_data folder if it does not exist
            os.mkdir(os.path.join(os.getcwd(), "chat_data"))
        if not Path(self.file_path).exists():  # Creating the chat file if it does not exist
            with open(self.file_path, 'w') as f:
                json.dump(dict(), f)  # Dumping the empty dictionary to the file

    def write(self, statuscode, client_name, msg):
        """This function is to write the msg to a file.
        statuscode = 0 if user receiving msg
        statuscode = 1 if user is sending the msg
        client_name: from which client the msg is received from or  send to"""
        with open(self.file_path, 'r+') as f:
            chat_dict = json.load(f)
            history = chat_dict.get(client_name, [])
            history.append((statuscode, msg))  # Since list is mutable, it will change in the dictionary too.
            chat_dict[client_name] = history
        with open(self.file_path, 'w') as f:
            json.dump(chat_dict, f)


def recievefromserver() -> None:
    """To receive data from the server"""
    global client
    while True:
        try:
            msg = client.recv(1024).decode("ascii")
            rec = jsondec(msg)["rec"]
            match rec:
                case "Nick":
                    client.send(jsonenc("Nick", nickname).encode("ascii"))
                case "msg":
                    sender_name, mesg = jsondec(msg)["data"]
                    print(f"msg received from {sender_name}:", mesg)
                    chat_handler.write(0, sender_name, mesg)
                    try: noti.show_toast(f"{sender_name}", mesg)
                    except: pass
                case "sync":
                    print("Starting to sync from the server")
                    export_import.import_data(jsondec(msg)["data"])

        except Exception as e:
            print("Closing Connection", e)
            client.close()
            del client
            break


def sendtoserver(reciever_name: str, msg: str) -> None:
    """To send the data to the server"""
    try:
        print("Sending", msg, "to", reciever_name)
        chat_handler.write(1, reciever_name, msg)
        client.send(jsonenc("msg", (nickname, msg)).encode("ascii"))

    except: pass


def sendThemeToServer() -> None:
    """To send the theme to the server"""
    data = (nickname, export_import.export(mode='to_server'))
    client.send(jsonenc("fsync", data).encode("ascii"))
    print('Trying to sync with server')


def requestSync() -> None:
    """To request the file of the user from the server"""
    client.send(jsonenc("sync", nickname).encode("ascii"))
    print('Trying to get the file from server')


def closeClient() -> None:
    """To close the connection of the client with the server"""
    client.close()


def startclient() -> None:
    """To start the process od connecting the client wth server"""
    global chat_handler
    client.connect((host, port))
    chat_handler = ChatHandler(nickname)
    threading.Thread(target = recievefromserver).start()
