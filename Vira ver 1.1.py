import time, initial_setup, history, tkinterlib
from tkinter import *
from pathlib import Path
#Checks if initial.vira exists...
#If it doesnt exist the initial setup is run.....
print("Checking for file 'initial.vira' ")
my_file = Path("initial.vira")
if my_file.exists():
    print("'initial.vira' found")
else:
    print("'initial.vira' not found")
    initial_setup.install_files()
    print('Necessary packages installed successfully')
#TODO:Make a function to automatically call imports and mention the status instead of using prinr(loaded) etc multiple times....

try:
    import tSK_ver_1 as task
    from talk1 import talk
    print("Loading themes")
    import theme
    print("loaded themes")
    import settings
    print('loaded settings.py,tsk_ver_1.py,talk1.py')
except Exception as e:
    print(e, "it seems some system files are missing")
    time.sleep(2)
    exit()
try:
    print('Indexing files')
    import indexer
    print('Indexed files')
except Exception as e:
    print(e)
    time.sleep(2)
    exit()
try:
    print("Loading usernames.py")
    import usernames

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
talk("I am Vira version 1 point 1")
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
#Read the theme from intial.vira
bg_colour, text_color, button_colour = theme.read_theme()
tkinterlib.tkinter_initialise(t1, 1200, 680)
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

        if keyword == "search" or keyword == "browse" or keyword == "srch":
            ord = ord.replace("search", "")
            ord = ord.replace("SEARCH", "")
            ord = ord.replace("browser", "")
            ord = ord.replace("srch", "")
            task.web(ord)

            history.user_file(name, ord,
                              f'"Opened Firefox and searched:" {ord}')
            print("Opened Firefox and searched:", ord)

        if "msg" == ord.lower() or "whatsapp" == ord.lower():
            task.whatsapp()
            history.user_file(name, ord, "Opened Whatsapp")

        if keyword in ['bye', 'tata', 'close', 'exit']:
            talk("Tata Bye Bye ")
            history.user_file(name, ord, "User closed")
            t1.destroy()
        if keyword in ['file', 'f']:
            indexer.search_indexed_file(afterkeyword)
            history.user_file(name, ord,
                              "Tried to open the file. Status:Unknown")
        if keyword == 'run':
            if afterkeyword in ['firefox', 'ff']:
                task.firefox()
            if afterkeyword in ['photoshop', 'ps']:
                task.photoshop()
            if afterkeyword in ['word', 'msword', 'doc']:
                task.msword()
            if afterkeyword in ['powerpoint', 'ppt']:
                task.powerpoint()
            if afterkeyword in ['vsc', 'vscode']:
                task.vscode()
            if afterkeyword in ['wa', 'msg', 'whatsapp']:
                task.whatsapp()
            if afterkeyword in ['wordpad', 'wp']:
                task.wordpad()
            if afterkeyword in [
                    'gimp',
            ]:
                task.gimp()
            if afterkeyword in [
                    'vlc',
            ]:
                task.vlc()
            if afterkeyword in ['telegram', 'tg']:
                task.telegram()
            history.user_file(name, ord, f"Opened {afterkeyword}")
        if "theme" in ord.lower():
            theme.theme_selector()
        if "firefox" in ord.lower():
            task.firefox()
            history.user_file(name, ord, "Opened firefox")

        if keyword == "settings" or keyword == "setting":
            talk('I have opened the settings page for you')
            settings.setting_page(name)
            history.user_file(name, ord, "Opened Settings")

        if "time" in ord.lower():
            task.tell_time()

            history.user_file(name, ord, "told Time ")

        if ord.lower() == "what is your version" or ord.lower() == "ver":
            talk("My version is 1 point 1")
            history.user_file(name, ord, "Vira Ver 1.1")

        if "what is your name" in ord.lower():
            talk("My name is vira and my version is 1.1")
            history.user_file(name, ord, "Told Vira version")

        if ord.lower() in ["hello", "hlo"]:
            talk("Hi")
            talk("What can i do for you")
            history.user_file(name, ord, "Greeted user")

        if ord.lower() == "hi":
            talk("Hello")
            talk("What can i do for you")
            history.user_file(name, ord, "Greeted user")

        if "download" in ord.lower():
            task.download()
            history.user_file(name, ord, "Opened downloads folder")

        if keyword in ["show history", 'sh']:
            history.user_file(name, ord, "Opened history")
            history.user_read(name)
            talk('Opened history')

        if ord.lower() == "clear history":
            history.clear_history(name)
            talk('Cleared history')

        if ord.lower() == "tell jokes" or ord.lower(
        ) == "tell a joke" or ord.lower() == "joke":
            task.joke()
            history.user_file(name, ord, f"Told joke'")

        ord == ""
        print("Over")


#Binds textbox so that if user presses enter work() is called
t1.bind("<Return>", work)
t1.mainloop()
#................command input and processing starts.....................
#................end of programme........................................
