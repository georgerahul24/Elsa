'''Created by George Rahul'''

from tkinter import *

import pyttsx3

from tSK_ver_1 import task
#Created by George Rahul
engine = pyttsx3.init()
voices = engine.getProperty('voices')  # getting details of current voice
# engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)  # changing index, changes voices. 1 for female

rate = engine.getProperty('rate')  # getting details of current speaking rate
engine.setProperty('rate', 150)  # setting up new voice rate




t=Tk()
t.geometry("1x1")
t.withdraw()
#t.deiconify() to make it appear again
win = Toplevel(t)
win.title("Vira Ver 2.0")
win.resizable(0,0)
win.geometry("300x300+500+250")
win.config(bg="light green")
win.attributes("-topmost",1)
#win.overrideredirect(1)

e=Entry(win,show="*",width=10)
e.place(x=104,y=60)

e1=Entry(win,width=10)
e1.place(x=104,y=40)
t1=Label(win,text="NAME:",bg="light green",font="Nebula").place(x=20,y=40)
t2=Label(win,text="PASSWORD:",bg="light green",font="Nebula 10 bold").place(x=0,y=60)

win1=Toplevel(t)
win1.withdraw()
win1.lift()
win1.attributes("-topmost",1)
e3=Entry(win1)









def new(nam):

    win.destroy()

    win1.title("Vira Ver2.0")
    win1.geometry("200x30+500+250")
    win1.deiconify()
    e3.pack()
    engine.say("Welcome " + nam)
    engine.say("What are your orders")
    engine.runAndWait()
    Label(win1,text="hello").pack()









def password(event):

    st=e.get()

    if "gr"==e.get():
        nam=e1.get()


        new(nam)


    else:

       engine.say("incorrect Password")
       engine.runAndWait()
       e1.delete(0,END)
       e.delete(0,END)
       button("verify")





def button(a):
    b = Button(win, text=a,  command= lambda:password("blah"))
    b.place(x=90, y=100)
  


button("Verify")
t.mainloop()
