import time
from tkinter import *
import tSK_ver_1 as task
from talk1 import *



try:
    print("Loading usernames.py")
    import usernames

    print("Loaded usernames.py is successfully")
    print("Starting to verify the module")
    usernames.verify_usernames()
    if usernames.verify_usernames.verify == False:
        print("Usernames.py verified successful")
    else:
        print("ERROR:Verification failed")
        time.sleep(2)
        exit()
except:
    print("ERROR:Could not load usernames.py")
    time.sleep(2)
    exit()
run_state = True
task.greeting()
print("Starting the security process")
print("\n")
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
        talk(f"Welcome {usernames.check_user.loginname}")

        break

    else:

        print("Access denied")
        security_trial += 1

        if security_trial >= 3:
            print("You have reached th maximum error limit")
            talk("You have reached the maximum error limit")
            talk("Bye Bye")
            time.sleep(2)
            exit()
        else:
            talk("Access denied")
            talk("please try again")

name = usernames.check_user.loginname

# ..............tkinter initialising starts...............................
t1 = Tk()
t1.withdraw()#hide the tkinter window to initialise logo,opacity etc
t1.overrideredirect(True)#remove borders
t1.attributes("-alpha", 0.6)

try:
    t1.iconbitmap(r'icon.ico')

except:
    talk("Sorry i couldnt open the icon..")

t1.attributes("-topmost", 1)
t1.title("Vira Version 1.1")
t1.resizable(0, 0)
t1.geometry("+1200+680")
eo = Entry(t1, bg="light green")
eo.pack()
t1.deiconify()#show the tkinter window back


# ..............tkinter initialising ends...............................

#................command input and processing starts.....................
def work(event):
    print("Work")
    ord = eo.get()
    eo.delete(0, END)
    parts=ord.split()
    if run_state == True:

        if parts[0].lower()=="search" or parts.lower()=="browse":
            ord = ord.replace("search", "")
            ord = ord.replace("SEARCH", "")
            ord = ord.replace("browser", "")
            task.web(ord)
            eo.delete(0, END)
            print("Opened Firefox and searched:",ord)

        if "msg" == ord.lower() or "whatsapp" == ord.lower():
            task.whatsapp()

        if "bye" == ord.lower() or "close" == ord.lower() or "exit" == ord.lower():
            talk("Tata Bye Bye ")
            t1.destroy()


        if "open" and " firefox" in ord.lower():
            task.firefox()
            eo.delete(0, END)
            print("I have opened Firefox")

        if "firefox" in ord.lower():
            task.firefox()
            eo.delete(0, END)
            print("I have opened Firefox")

        if "open wordpad" in ord.lower():
            task.wordpad()
            eo.delete(0, END)
            print("I have opened Wordpad")

        if "time" in ord.lower():
            task.tell_time()
            eo.delete(0, END)

        if "open gimp" in ord.lower():
            task.gimp()
            eo.delete(0, END)

        if "what is your version" in ord.lower():
            talk("My version is 1 point 1")
            eo.delete(0, END)

        if "what is your name" in ord.lower():
            talk("My name is vira and my version is 1.1")

        if "hlo" in ord.lower():
            talk("Hello")
            talk("What can i do for you")

            eo.delete(0, END)

        if "hello" in ord.lower():
            talk("Hi")
            talk("What can i do for you")
            eo.delete(0, END)

        if "hi" in ord.lower():
            talk("Hello")
            talk("What can i do for you")
            eo.delete(0, END)

        if "download" in ord.lower():
            task.download()

        ord == ""
        print("Over")


t1.bind("<Return>", work)

t1.mainloop()
#................command input and processing starts.....................
#................end of programme........................................