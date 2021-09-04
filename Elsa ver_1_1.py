"""
Version 1.1.231 (multithreading enabled)
"""
import os
from functools import partial
from threading import Thread
from pathlib import Path
from tkinter import Tk, Entry, END

try:
    print("Importing the package 'Magic'")
    from Magic import initial_setup

    print("Successfully imported initial_setup")

    # Checks if initial.elsa exists...
    # If it doesnt exist the initial setup is run.....
    print("Checking for file 'initial.elsa' ")
    initpth = os.getcwd() + "\\resources\\ initial.elsa"
    initial_file = Path(initpth)
    if initial_file.exists():
        print("'initial.elsa' found")
    else:
        print("'initial.elsa' not found")
        initial_setup.install_files()
        print("Necessary files installed successfully")
    from Magic import (
        history,
        tkinterlib,
        popups,
        program_run,
        theme,
        settings,
        indexer,
        usernames,
        highlighter,
    )

    print(
        "history,tkinterlib,srchpopup,program_run,theme,settings,indexer and usernames imported from Magic"
    )

except Exception as e:
    print("Error loading Magic", e)
    print(
        "Suggested fix:install/update magicForElsa using pip install --upgrade magicForElsa"
        "or reinstall the elsa ver1_1.py file from https://github.com/georgerahul24/Viraver1.1"
    )
    input("Press any key to exit....")

    exit()

# Reading the themes for the tkinter window and all
bg_colour, text_color, button_colour = theme.read_theme()
try:
    print("loading task and talk modules")
    from task1 import task
    from talk1.talk1 import talk

    print("Loaded task and talk modules successfully")
except Exception as e:
    print(e, "it seems there some problem with task1 and/or talk1 package")
    print(
        "Suggested fix:install/update magicForElsa using pip install --upgrade magicForElsa"
        "or reinstall the elsa ver1_1.py file from https://github.com/georgerahul24/Viraver1.1"
    )
    input("Press any key to exit....")
    exit()
# verifying usernames module
print("Starting to verify the integrity username module")
CHK = usernames.verify_usernames()
# see how 'not' operator works with 'if' in https://pythonexamples.org/python-if-not/
if not CHK:
    print("'Usernames.py' verified successfully")
else:
    print("ERROR:Verification failed")
    print(
        "Suggested fix:install/update magicForElsa using pip install --upgrade magicForElsa"
        "or reinstall the elsa ver1_1.py file from https://github.com/georgerahul24/Viraver1.1"
    )
    input("Press any key to exit....")
    exit()

RUN_STATE = True
print("Starting to verify the user")
talk("Hi. I am Elsa")
SECURITY_TRIAL = 0


def quit(event="") -> None:
    """
    To exit the program
    :param event: Not imp
    :type event: str
    :return:None
    :rtype: None
    """
    talk("Tata Bye Bye ")
    history.user_file(name, ord, "User closed")
    exit()


# password and username checks
while True:
    usernames.check_user()
    if usernames.check_user.security:
        print("Access Granted")
        talk("Access Granted")
        task.greeting(usernames.check_user.loginname)
        break

    else:
        print("Access Denied")
        SECURITY_TRIAL += 1
        if SECURITY_TRIAL >= 3:
            print("You have reached the maximum error limit")
            talk("You have reached the maximum error limit")
            exit()
        else:
            talk("Access Denied")
            talk("Please Try Again")
name = usernames.check_user.loginname
# ..............tkinter initialising starts...............................
elsagui = Tk()
# Reading the screen height and width
screen_height, screen_width = elsagui.winfo_screenheight(
), elsagui.winfo_screenwidth()
tkinterlib.tkinter_initialise(elsagui, screen_width - 150, screen_height - 100)
Search_box = Entry(elsagui, bg=bg_colour, fg=text_color)
Search_box.pack()

# ..............tkinter initialising ends...............................


# ................command input and processing starts.....................
def work(event="") -> None:
    """
    This is the main function where user input is read and proper actions are taken
    :param event: not imp
    :type event: str
    :return: None
    :rtype: None
    """
    ord = Search_box.get()
    Search_box.delete(0, END)
    parts = ord.split()
    keyword = parts[0]
    afterword = ""
    try:
        for index in range(1, len(parts)):
            afterword += " " + parts[index]

        afterword = afterword.lower().lstrip()

    except:
        afterword = ""

    keyword = keyword.lower()

    if RUN_STATE:
        # srch in net
        if keyword in ["search", "browse", "srch", "s"]:

            newThread = Thread(target=task.web, args=(afterword, ))
            newThread.start()
            history.user_file(name, ord, f'"Searched:" {ord}')

        elif ord.lower() in ["msg", "whatsapp"]:

            newThread = Thread(target=task.whatsapp)
            newThread.start()
            history.user_file(name, ord, "Opened Whatsapp")
        elif keyword in ["bye", "tata", "close", "exit"]:
            quit()
        elif keyword in ["file", "f"]:

            newThread = Thread(target=indexer.search_indexed_file,
                               args=(afterword, ))
            newThread.start()

            history.user_file(name, ord,
                              "Tried to open the file. Status:Unknown")
        elif keyword == "run":

            newThread = Thread(target=program_run.program_run,
                               args=(afterword, ))
            newThread.start()

            history.user_file(name, ord, f"Opened {afterword}")
        elif "theme" in ord.lower():
            theme.theme_selector()
        elif "firefox" in ord.lower():
            newThread = Thread(target=task.firefox)
            newThread.start()

            history.user_file(name, ord, "Opened firefox")
        elif keyword in ["settings", "setting"]:
            talk("I have opened the settings page for you")
            settings.setting_page(name)

            history.user_file(name, ord, "Opened Settings")
        elif keyword == "time":
            task.tell_time()
            history.user_file(name, ord, "told Time ")

        elif ord.lower() in ["what is your version", "ver"]:
            talk("My version is 1 point 1")
            history.user_file(name, ord, "Elsa Ver 1.1")

        elif "what is your name" in ord.lower():
            talk("My name is Elsa")
            history.user_file(name, ord, "Told version of Elsa")

        elif ord.lower() in ["hello", "hlo", "hey"]:
            talk("Hi. What can I do for you")

            history.user_file(name, ord, "Greeted user")

        elif ord.lower() == "hi":
            talk(f"Hello {name}")

            history.user_file(name, ord, "Greeted user")
        elif "download" in ord.lower():
            task.download()
            history.user_file(name, ord, "Opened downloads folder")
        elif "desktop" in ord.lower():
            task.desktop()
            history.user_file(name, ord, "Opened desktop folder")
        elif "music" in ord.lower():
            task.musicFolder()
            history.user_file(name, ord, "Opened music folder")

        elif keyword in ["show history", "sh"]:
            history.user_file(name, ord, "Opened history")
            history.user_read(username=name)
            talk("Opened history")
        elif ord.lower() == "clear history":
            history.clear_history(name)
            talk("Cleared history")
        elif ord.lower() in ["tell jokes", "tell a joke", "joke"]:
            task.joke()
            history.user_file(name, ord, "Told a joke")

        elif keyword == "shutdown":
            history.user_file(name, ord, "Shutdown the computer")
            task.shutdown()
        elif keyword == "restart":
            history.user_file(name, ord, "Restarted the computer")
            task.restart()
        else:

            def srchUserInput():
                talk(
                    "I could not understand what you meant. Do you wanna find it in the internet?"
                )
                popups.popups(ord)

            newThread = Thread(target=srchUserInput)
            newThread.start()
            history.user_file(name, ord, f"Searched {ord} in internet")


def clearTextbox(event=""):
    Search_box.delete(0, END)


# Binding keyboard shortcuts
elsagui.bind("<Control-h>", partial(history.user_read, username=name))
elsagui.bind("<Control-e>", quit)
elsagui.bind("<Control-t>", theme.theme_selector)
elsagui.bind("<Control-s>",
             partial(settings.setting_page, username=name, state=True))
# syntax highlighting
elsagui.bind("<KeyRelease>",
             partial(highlighter.syntax_highlighting, Search_box=Search_box))
# Binds textbox so that if user presses enter work() is called
elsagui.bind("<Return>", work)
elsagui.bind("<Control-BackSpace>", clearTextbox)
elsagui.mainloop()
# ................command input and processing starts.....................
# ................end of programme........................................
