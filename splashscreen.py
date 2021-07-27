from tkinter import *

s=Tk()
def splash_screen():


    s.geometry("+1200+680")
    s.overrideredirect(True)
    s.attributes("-topmost", 1)

    l=Label(s,text="Vira 1.1").pack()
    l1=Label(s,text="loading").pack()
    s.mainloop()


def destroy():
    print('tkinter destroyed')
    Label(s,text='hello').pack()
    s.withdraw()
    s.destroy()
