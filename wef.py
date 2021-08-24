from tkinter import *
import tkinterlib

t1 = Tk()
#Read the theme from intial.elsa
screen_height = t1.winfo_screenheight()
screen_width = t1.winfo_screenwidth()
print(screen_width, screen_width)
tkinterlib.tkinter_initialise(t1, screen_width - 100, screen_height - 500)
Label(t1, text='hi').pack()
t1.mainloop()
