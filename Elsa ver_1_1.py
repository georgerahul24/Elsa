import time
import Magic.initial_setup as initial_setup
import Magic.history as history
import Magic.tkinterlib as tkinterlib
from tkinter import *
from pathlib import Path
from functools import partial
#Checks if initial.elsa exists...
#If it doesnt exist the initial setup is run.....
print("Checking for file 'initial.elsa' ")
initial_file = Path("initial.elsa")
if initial_file.exists():
    print("'initial.elsa' found")
else:
    print("'initial.elsa' not found")
    initial_setup.install_files()
    print('Necessary packages installed successfully')

print("Loading themes")
import Magic.theme as theme

print("loaded themes")

print("Importing popups")
import Magic.srchpopup as srchpopup

print("Popups imported")
bg_colour, text_color, button_colour = theme.read_theme()
#...splash screen........
splashscr = Tk()
tkinterlib.tkinter_initialise(splashscr, 350, 300)
splash = LabelFrame(splashscr, text="Loading", bg=bg_colour, fg=text_color)
splash.pack()

l = Label(splash,
          text="Elsa 1.1.150",
          bg=bg_colour,
          fg=text_color,
          font="nebula 100 bold").pack()
splash.after(3000, splashscr.destroy)
splash.mainloop()
#...splash screen ends........

try:
    from task1 import task
    from talk1.talk1 import talk

    import Magic.settings as settings
    print('loaded settings.py,task,talk1')
except Exception as e:
    print(e, "it seems some system files are missing")
    time.sleep(2)
    exit()
try:
    print('Indexing files')
    import Magic.indexer as indexer
    print('Indexing complete')
except Exception as e:
    print(e)
    time.sleep(2)
    exit()
try:
    print("Loading usernames.py")
    import Magic.usernames as usernames

    print("Loaded usernames.py is successfully")
    print("Starting to verify the module")
    usernames.verify_usernames()
    if usernames.verify_usernames.verify == False:
        print("'Usernames.py' verified successfully")
    else:
        print("ERROR:Verification failed")
        time.sleep(2)
        exit()
except:
    print("ERROR:Could not load usernames.py")
    time.sleep(2)
    exit()
run_state = True

print("Starting to verify the user")
talk("Hello")
talk("I am Elsa version 1 point 1")
security_state = True
security_trial = 0

# password and username checks
while security_state == True:
    usernames.check_user()
    if usernames.check_user.security == True:

        print("Access Granted")
        talk("Access Granted")
        task.greeting(usernames.check_user.loginname)

        break

    else:

        print("Access Denied")
        security_trial += 1

        if security_trial >= 3:
            print("You have reached th maximum error limit")
            talk("You have reached the maximum error limit")
            talk("Bye Bye")
            time.sleep(2)
            exit()
        else:
            talk("Access Denied")
            talk("Please Try Again")

name = usernames.check_user.loginname

# ..............tkinter initialising starts...............................
t1 = Tk()
#Read the theme from intial.elsa
screen_height = t1.winfo_screenheight()
screen_width = t1.winfo_screenwidth()
tkinterlib.tkinter_initialise(t1, screen_width - 150, screen_height - 100)
eo = Entry(t1, bg=bg_colour, fg=text_color)
eo.pack()

# ..............tkinter initialising ends...............................


#................command input and processing starts.....................
def work(event):
    ord = eo.get()
    eo.delete(0, END)
    parts = ord.split()
    keyword = parts[0]
    try:
        afterkeyword = parts[1]
        afterkeyword = afterkeyword.lower()
    except:
        pass
    keyword = keyword.lower()

    if run_state == True:
        #srch in net
        if keyword == "search" or keyword == "browse" or keyword == "srch":
            ord = ord.replace("search", "")
            ord = ord.replace("SEARCH", "")
            ord = ord.replace("browser", "")
            ord = ord.replace("srch", "")
            task.web(ord)

            history.user_file(name, ord,
                              f'"Searched:" {ord}')

        #open whatsapp......
        elif "msg" == ord.lower() or "whatsapp" == ord.lower():
            task.whatsapp()
            history.user_file(name, ord, "Opened Whatsapp")
        #end the program
        elif keyword in ['bye', 'tata', 'close', 'exit']:
            talk("Tata Bye Bye ")
            history.user_file(name, ord, "User closed")
            exit()
        #open files....
        elif keyword in ['file', 'f']:
            indexer.search_indexed_file(afterkeyword)
            history.user_file(name, ord,
                              "Tried to open the file. Status:Unknown")
        #open programs......
        elif keyword == 'run':
            if afterkeyword in ['firefox', 'ff']:
                task.firefox()
            elif afterkeyword in ['photoshop', 'ps']:
                task.photoshop()
            elif afterkeyword in ['word', 'msword', 'doc']:
                task.msword()
            elif afterkeyword in ['powerpoint', 'ppt']:
                task.powerpoint()
            elif afterkeyword in ['vsc', 'vscode']:
                task.vscode()
            elif afterkeyword in ['wa', 'msg', 'whatsapp']:
                task.whatsapp()
            elif afterkeyword in ['wordpad', 'wp']:
                task.wordpad()
            elif afterkeyword in [
                    'gimp',
            ]:
                task.gimp()
            elif afterkeyword in [
                    'vlc',
            ]:
                task.vlc()
            elif afterkeyword in ['telegram', 'tg']:
                task.telegram()
            history.user_file(name, ord, f"Opened {afterkeyword}")
        #..select a new theme.....
        elif "theme" in ord.lower():
            theme.theme_selector()
        #...open firefox
        elif "firefox" in ord.lower():
            task.firefox()
            history.user_file(name, ord, "Opened firefox")
        #settings page.....
        elif keyword == "settings" or keyword == "setting":
            talk('I have opened the settings page for you')
            settings.setting_page(name)
            history.user_file(name, ord, "Opened Settings")
        #....wishes,time and questions....
        elif "time" in ord.lower():
            task.tell_time()

            history.user_file(name, ord, "told Time ")

        elif ord.lower() == "what is your version" or ord.lower() == "ver":
            talk("My version is 1 point 1")
            history.user_file(name, ord, "Elsa Ver 1.1")

        elif "what is your name" in ord.lower():
            talk("My name is Elsa and my version is 1.1")
            history.user_file(name, ord, "Told version of Elsa")

        elif ord.lower() in ["hello", "hlo", 'hey']:
            talk("Hi")

            history.user_file(name, ord, "Greated user")

        elif ord.lower() == "hi":
            talk("Hello")
            talk("What can i do for you")
            history.user_file(name, ord, "Greated user")
        #opening folders
        elif "download" in ord.lower():
            task.download()
            history.user_file(name, ord, "Opened downloads folder")
        elif "desktop" in ord.lower():
            task.desktop()
            history.user_file(name, ord, "Opened desktop folder")
        elif "music" in ord.lower():
            task.musicFolder()
            history.user_file(name, ord, "Opened music folder")

        #...history settings.......
        elif keyword in ["show history", 'sh']:
            history.user_file(name, ord, "Opened history")
            history.user_read(username=name)
            talk('Opened history')

        elif ord.lower() == "clear history":
            history.clear_history(name)
            talk('Cleared history')
        #....jokes..........
        elif ord.lower() == "tell jokes" or ord.lower(
        ) == "tell a joke" or ord.lower() == "joke":
            task.joke()
            history.user_file(name, ord, f"Told joke")

        #...shutting down and restarting......
        elif keyword == "shutdown":
            history.user_file(name, ord, f"Shutdown the computer")
            task.shutdown()
        elif keyword == "restart":
            history.user_file(name, ord, f"Restarted the computer")
            task.restart()
        else:
            talk(
                'I could not understand what you meant. Do you wanna find it in the internet?'
            )
            srchpopup.popups(ord)

            history.user_file(name, ord, f"Searched {ord} in internet")
        #Destroy in case any yes or no popups are there


        try:
            srchpopup.popups.destroyPop()
        except:
            pass


#Binding keyboard shortcuts
t1.bind("<Control-h>", partial(history.user_read, username=name))
t1.bind("<Control-t>", theme.theme_selector)
t1.bind("<Control-s>", partial(settings.setting_page,
                               username=name,
                               state=True))
#Binds textbox so that if user presses enter work() is called
t1.bind("<Return>", work)
t1.mainloop()
#................command input and processing starts.....................
#................end of programme........................................
