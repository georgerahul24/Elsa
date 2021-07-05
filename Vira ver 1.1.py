from tkinter import *
import pyttsx3

from tSK_ver_1 import task

engine = pyttsx3.init()
voices = engine.getProperty('voices')  # getting details of current voice
# engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)  # changing index, changes voices. 1 for female

rate = engine.getProperty('rate')  # getting details of current speaking rate
engine.setProperty('rate', 120)  # setting up new voice rate

t1 = Tk()
t1.withdraw()
t1.attributes("-alpha", 0.7)

try:
    t1.iconbitmap(r'icon.ico')

except:
    engine.say("Sorry i couldnt open the icon..")
    engine.runAndWait()


t1.attributes("-topmost", 1)
t1.title("Vira Version 1.1")
t1.resizable(0, 0)
t1.geometry("+1200+680")
eo = Entry(t1, bg="light green")
eo.pack()

a = True

task.greeting()

t1.deiconify()



def work(event):
    print("Work")
    ord = eo.get()

    eo.delete(0, END)
    if a == True:



        if "search" in ord.lower():
            ord = ord.replace("search", "")
            ord = ord.replace("SEARCH", "")
            ord = ord.replace("browser", "")
            task.web(ord)
            eo.delete(0, END)
            print("I have opened Firefox")
        if "browse" in ord.lower():
            ord = ord.replace("search", "")
            ord = ord.replace("SEARCH", "")
            ord = ord.replace("browse", "")
            task.web(ord)
            eo.delete(0, END)
            print("I have opened Firefox")
        if "msg" ==  ord.lower():
            task.whatsapp()
        if "whatsapp" ==  ord.lower():
            task.whatsapp()
            
        if "bye" == ord.lower():
            engine.say(" Tata Bye Bye ")


            engine.runAndWait()
            t1.destroy()
        if "close" == ord.lower():
            engine.say(" Tata Bye Bye ")
            engine.runAndWait()
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
        if "open dreamweaver" in ord.lower():
            task.dreamweaver()
            eo.delete(0, END)
        if "open gimp" in ord.lower():
            task.gimp()
            eo.delete(0, END)
        if "open photoshop" in ord.lower():
            task.photoshop()
            eo.delete(0, END)


        if "who is your father" in ord.lower():
            print("i was created by George")
            engine.say("i was created by George")
            engine.runAndWait()
            eo.delete(0, END)

        if "what is your version" in ord.lower():
            engine.say("My version is 1 point 1")
            engine.runAndWait()
            eo.delete(0, END)
        if "what is your name" in ord.lower():
            print("My name is vira and my version is 1.1")
            engine.say("My name is vira and my version is 1.1")
            engine.runAndWait()
        if "hlo" in ord.lower():
            print("Hello")
            engine.say("Hello")
            engine.say("What can i do for you")
            engine.runAndWait()
            eo.delete(0, END)

        if "hello" in ord.lower():
            print("Hello")
            engine.say("Hello")
            engine.say("What can i do for you")

            engine.runAndWait()
            eo.delete(0, END)

        if "hi" in ord.lower():
            print("Hello")
            engine.say("Hello")
            engine.say("What can i do for you")
            engine.runAndWait()
            eo.delete(0, END)
        if "study" in ord.lower():
            task.study()
        if "brilli" in ord.lower():
            task.brilli()
        if "down" in ord.lower():
            task.download()
        if "story" in ord.lower():
            task.story_books()
        ord == ""
        print("Over")


t1.bind("<Return>", work)

t1.mainloop()
