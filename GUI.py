'''Created by George Rahul'''

from tkinter import *

import pyttsx3

# Created by George Rahul
engine = pyttsx3.init()
voices = engine.getProperty('voices')  # getting details of current voice
# engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)  # changing index, changes voices. 1 for female

rate = engine.getProperty('rate')  # getting details of current speaking rate
engine.setProperty('rate', 150)  # setting up new voice rate
def SecurityUI():

    t = Tk()
    t.geometry("1x1")
    t.iconbitmap(r'icon.ico')
    t.withdraw()
    # t.deiconify() to make it appear again
    win = Toplevel(t)
    win.title("Vira Ver 1.1")
    win.resizable(0, 0)
    win.geometry("300x300+500+250")
    win.config(bg="light green")
    win.attributes("-topmost", 1)
    win.iconbitmap(r'icon.ico')
    # win.overrideredirect(1)

    e = Entry(win, show="*", width=10)
    e.place(x=104, y=60)

    e1 = Entry(win, width=10)
    e1.place(x=104, y=40)
    t1 = Label(win, text="Username:", bg="light green", font="Nebula 10 bold").place(x=20, y=40)
    t2 = Label(win, text="Password:", bg="light green", font="Nebula 10 bold").place(x=20, y=60)

    win1 = Toplevel(t)
    win1.withdraw()
    win1.lift()
    win1.attributes("-topmost", 1)
    e3 = Entry(win1)


    def password(event):
        password.passgui = e.get()
        password.usergui = e1.get()

        t.destroy()



    def button(a):
        b = Button(win, text=a, command=lambda:password("blah"))
        b.place(x=90, y=100)


    button("Verify")
    t.mainloop()
    return password.usergui, password.passgui

if __name__=="__main__":
    SecurityUI()