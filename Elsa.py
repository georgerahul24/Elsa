import gc
import os
from functools import partial
from pathlib import Path
from threading import Thread
from tkinter import Tk, Entry, END
import elsabackend
from elsabackend import quit, print_talk
import updater
updater.updater()
gc.disable()  # disabling garbage collection as it causes problem with tkinter threads


def loading_error_warning(e: Exception = '') -> None:
    """To load the warning and then exit out of the program"""
    print(e,
          "It seems there some problem with task1 and/or talk1 package and/or magic package and/or the main file is outdated")
    print("Suggested fix:install/update magicForElsa using pip install --upgrade magicForElsa"
          "or reinstall the elsa ver1_1.py file from https://github.com/georgerahul24/Viraver1.1")
    exit(input("Press any key to exit...."))


try:
    from Magic import initial_setup

    # Checks if initial.elsa exists.If it doesn't exist the initial setup is run.....
    initial_file = Path((os.getcwd() + "\\resources\\ initial.elsa"))
    print("'initial.elsa' found") if initial_file.exists() else initial_setup.install_files()
    from Magic import (history, tkinterlib, popups, program_run, theme, settings, indexer, usernames, highlighter,
                       chat_client)

    indexer.index_files()
except Exception as e:
    loading_error_warning(e)
# Reading the themes for the tkinter window and all
bg_colour, text_color, button_colour = theme.read_theme()
try:
    from task1 import task
    from talk1.talk1 import talk
except Exception as e:
    loading_error_warning(e)
# verifying usernames module
CHK = usernames.verify_usernames()
# see how 'not' operator works with 'if' in https://pythonexamples.org/python-if-not/
if os.environ["USERPROFILE"] != 'C:\\Users\\George Rahul':
    print("'Usernames.py' verified successfully") if not CHK else loading_error_warning()
    print_talk("Starting the login page", "Hi. I am Elsa")
    SECURITY_TRIAL = 0
    # password and username checks
    while True:
        usernames.check_user()
        if usernames.check_user.security:
            print_talk("Access Granted", "Access Granted")
            task.greeting(usernames.check_user.loginname)
            break
        else:
            print("Access Denied")
            SECURITY_TRIAL += 1
            if SECURITY_TRIAL >= 3:
                exit(print_talk("You have reached the maximum error limit", "You have reached the maximum error limit"))
            else:
                print_talk("Access Denied. Please Try Again", "Access Denied. Please Try Again")
    name = usernames.check_user.loginname
else:
    name,SECURITY_TRIAL = 'admin',0
del CHK, SECURITY_TRIAL
# ..............tkinter initialising starts...............................
elsagui = Tk()
# Reading the screen height and width
screen_height, screen_width = elsagui.winfo_screenheight(), elsagui.winfo_screenwidth()
tkinterlib.tkinter_initialise(elsagui, screen_width - 150, screen_height - 100)
Search_box = Entry(elsagui, bg = bg_colour, fg = text_color)
Search_box.pack()
# ..............tkinter initialising ends...............................
# ...initialising chat client..........
chat_client.getNickname(name)

try:
    print("Connecting to a server")
    chat_client.startclient()
    print("Connected to a server")
except:
    print("Could not establish a connection with server")
backend1list = elsabackend.get_keywords()


# .....initialising reminder...


def clearTextbox(event = "") -> None:
    """To clear the textbox"""
    Search_box.delete(0, END)


# ................command input and processing starts.....................
def work(event = "") -> None:
    """This is the main function where user input is read and proper actions are taken"""
    order = Search_box.get().lower()
    clearTextbox()
    parts = order.split(maxsplit = 1)
    if len(parts) < 2: parts += ['', ]
    keyword, afterword = parts[0], parts[1]
    parts=order.split()

    match keyword:
        case "search" | "browse" | "srch" | "s":
            Thread(target = task.web, args = (afterword,)).start()
            history.user_file(name, order, f'"Searched:" {order}')
        case "msg":
            chat_client.sendtoserver(nameToSend := parts[1], msgTosend := " ".join(parts[2:]))
            history.user_file(name, order, f"Snd msg to {nameToSend}.Msg was {msgTosend}")
        case "open" | "o" | "folder":
            Thread(target = indexer.search_indexed_folder, args = (afterword,)).start()
            history.user_file(name, order, f"Tried to open the folder {afterword}. Status:Unknown")
        case "file" | "f":
            Thread(target = indexer.search_indexed_file, args = (afterword,)).start()
            history.user_file(name, order, f"Tried to open the file {afterword}. Status:Unknown")
        case "run":
            Thread(target = program_run.program_run, args = (afterword,)).start()
            history.user_file(name, order, f"Opened {afterword}")
        case "firefox":
            Thread(target = task.firefox).start()
            history.user_file(name, order, "Opened firefox")
        case "settings" | "setting":
            talk("I have opened the settings page for you")
            settings.setting_page(name)
            history.user_file(name, order, "Opened Settings")
        case "website" | "w":
            task.websiteopen(afterword)
            history.user_file(name, order, f"Tried to open the website {afterword}")

        case "hello" | "hlo" | "hey":
            talk("Hi. What can I do for you")
        case "hi":
            talk(f"Hello {name}")
        case _:
            match order:
                case "what is your version" | "ver":
                    talk("My version is 1 point 1")
                case "what is your name":
                    talk("My name is Elsa")
                case "show history" | "sh":
                    history.user_read(username = name)
                    talk("Opened history")
                case "clear history":
                    history.clear_history(name)
                    talk("Cleared history")
                case "shutdown":
                    history.user_file(name, order, "Shutdown the computer")
                    task.shutdown()
                case "restart":
                    history.user_file(name, order, "Restarted the computer")
                    task.restart()
                case _:
                    if order in backend1list:
                        elsabackend.backend1_1(order, name)
                    else:
                        def srchUserInput():
                            print_talk(tal = "I could not understand what you meant. Do you wanna find it in the internet?")
                            popups.popups(order)

                        Thread(target = srchUserInput).start()
                        history.user_file(name, order, f"Tried to search {order} in internet.Status unknown")

    del parts, keyword, afterword
    gc.collect()


# Binding keyboard shortcuts
[elsagui.bind(i[0], i[1]) for i in [("<Control-h>", partial(history.user_read, username = name)), ("<Control-e>", quit),
                                    ("<Control-s>", partial(settings.setting_page, username = name, state = True)),
                                    ("<KeyRelease>", partial(highlighter.syntax_highlighting, Search_box = Search_box)),
                                    ("<Return>", work),
                                    ("<Control-BackSpace>", clearTextbox)]]
elsagui.mainloop()
