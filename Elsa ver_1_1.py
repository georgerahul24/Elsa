import os
import time
from functools import partial
from pathlib import Path
from tkinter import Tk, Entry, END

try:
    print("Importing the package 'Magic'")
    from Magic import initial_setup

    print(
        'Successfully imported initial_setup,history,'
        'tkinterlib,srchpopup,program_run,theme,settings,indexer and usernames from Magic'
    )

    # Checks if initial.elsa exists...
    # If it doesnt exist the initial setup is run.....
    print("Checking for file 'initial.elsa' ")
    initpth = os.getcwd() + '\\resources\\ initial.elsa'
    initial_file = Path(initpth)
    if initial_file.exists():
        print("'initial.elsa' found")
    else:
        print("'initial.elsa' not found")
        initial_setup.install_files()
        print('Necessary packages installed successfully')
    from Magic import history, tkinterlib, srchpopup, program_run, theme, settings, indexer, usernames
except Exception as e:
    print('Error loading Magic', e)
    time.sleep(5)
    exit()

# Reading the themes for the tkinter window and all
bg_colour, text_color, button_colour = theme.read_theme()
try:
    print('loading task and talk')
    from task1 import task
    from talk1.talk1 import talk

    print('Loaded task and talk')
except Exception as e:
    print(e, "it seems there some problem with task1 or talk1")
    time.sleep(5)
    exit()
# verifying usernames module
print("Starting to verify username module")
CHK = usernames.verify_usernames()
print("Checking username")
# see how 'not' operator works with 'if' in https://pythonexamples.org/python-if-not/
if not CHK:
    print("'Usernames.py' verified successfully")
else:
    print("ERROR:Verification failed")
    time.sleep(2)
    exit()
RUN_STATE = True
print("Starting to verify the user")
talk("Hello. I am Elsa version 1 point 1")
SECURITY_STATE = True
SECURITY_TRIAL = 0


def quit(event=""):
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
while SECURITY_STATE:
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
            quit()
        else:
            talk("Access Denied")
            talk("Please Try Again")
name = usernames.check_user.loginname
# ..............tkinter initialising starts...............................
t1 = Tk()
# Reading the screen height and width
screen_height, screen_width = t1.winfo_screenheight(), t1.winfo_screenwidth()
tkinterlib.tkinter_initialise(t1, screen_width - 150, screen_height - 100)
Search_box = Entry(t1, bg=bg_colour, fg=text_color)
Search_box.pack()


# ..............tkinter initialising ends...............................


# ................command input and processing starts.....................
def work(event=""):
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
    try:
        afterword = parts[1]
        afterword = afterword.lower()
    except:
        afterword = ''
    keyword = keyword.lower()

    if RUN_STATE:
        # srch in net
        if keyword in ["search", "browse", "srch"]:
            # To remove the srch,search,etc words before searching with web()
            ord = task.ordShortenSrch(ord)
            task.web(ord)
            history.user_file(name, ord, f'"Searched:" {ord}')

        elif ord.lower() in ["msg", "whatsapp"]:
            task.whatsapp()
            history.user_file(name, ord, "Opened Whatsapp")
        elif keyword in ['bye', 'tata', 'close', 'exit']:
            quit()
        elif keyword in ['file', 'f']:
            indexer.search_indexed_file(afterword)
            history.user_file(name, ord,
                              "Tried to open the file. Status:Unknown")
        elif keyword == 'run':
            program_run.program_run(afterword)
            history.user_file(name, ord, f"Opened {afterword}")
        elif "theme" in ord.lower():
            theme.theme_selector()
        elif "firefox" in ord.lower():
            task.firefox()
            history.user_file(name, ord, "Opened firefox")
        elif keyword in ["settings", "setting"]:
            talk('I have opened the settings page for you')
            settings.setting_page(name)
            history.user_file(name, ord, "Opened Settings")
        elif "time" in ord.lower():
            task.tell_time()
            history.user_file(name, ord, "told Time ")

        elif ord.lower() in ["what is your version", "ver"]:
            talk("My version is 1 point 1")
            history.user_file(name, ord, "Elsa Ver 1.1")

        elif "what is your name" in ord.lower():
            talk("My name is Elsa and my version is 1.1")
            history.user_file(name, ord, "Told version of Elsa")

        elif ord.lower() in ["hello", "hlo", 'hey']:
            talk("Hi")

            history.user_file(name, ord, "Greeted user")

        elif ord.lower() == "hi":
            talk("Hello")
            talk("What can i do for you")
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

        elif keyword in ["show history", 'sh']:
            history.user_file(name, ord, "Opened history")
            history.user_read(username=name)
            talk('Opened history')

        elif ord.lower() == "clear history":
            history.clear_history(name)
            talk('Cleared history')
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
            talk(
                'I could not understand what you meant. Do you wanna find it in the internet?'
            )
            srchpopup.popups(ord)

            history.user_file(name, ord, f"Searched {ord} in internet")
        # Destroy in case any yes or no popups are there


# syntax highlighting
def syntax_highlighting(event=''):
    try:
        ord = Search_box.get()

        keyword = ord.split()[0]
        keywords = [
            'run', 'f', 'open', 'file', 'hi', 'hello', 'bye', 'tata',
            'shutdown', 'restart', 'sh', 'show', 'clear', 'exit', 'msg', 'whatsapp', 'theme', 'firefox', 'music',
            'desktop', 'joke,'

        ]
        if keyword in keywords:
            Search_box.delete(0, END)
            Search_box.config(fg='light green')
        else:
            Search_box.delete(0, END)
            Search_box.config(fg=text_color)
        Search_box.insert(0, ord)
    except:
        pass


# Binding keyboard shortcuts
t1.bind("<Control-h>", partial(history.user_read, username=name))
t1.bind("<Control-e>", quit)
t1.bind("<Control-t>", theme.theme_selector)
t1.bind("<Control-s>", partial(settings.setting_page,
                               username=name,
                               state=True))
t1.bind('<KeyRelease>', syntax_highlighting)
# Binds textbox so that if user presses enter work() is called
t1.bind("<Return>", work)
t1.mainloop()
# ................command input and processing starts.....................
# ................end of programme........................................
