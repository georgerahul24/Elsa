#............Austin has reserved this space..............................

from tkinter import *

s = Tk()


def splash_screen():

    #tkinter labels
    s.geometry("+500+300")
    s.overrideredirect(True)
    s.attributes("-topmost", 1)

    l = Label(s, text="Vira 1.1", fg="green").pack()
    l1 = Label(s, text="loading", bg="green").pack()
    l2 = Label(s, text="George is great", bg="black", fg="yellow").pack()
    s.mainloop()


splash_screen()
