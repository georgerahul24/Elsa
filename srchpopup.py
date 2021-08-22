from tkinter import *
from tSK_ver_1 import web
import tkinterlib,theme

def popups(srch):
    popups=Tk()
    bg_colour, text_color, button_colour = theme.read_theme()
    tkinterlib.tkinter_initialise(popups,x=1230,y=650)
    def srchYes(event=''):
        popups.destroy()
        web(srch)
    Yes=Button(popups,text='Yes',bg=button_colour,fg=text_color,command=srchYes)

    No = Button(popups,text='No', bg=button_colour, fg=text_color,command=popups.destroy)
    Yes.grid(row=1,column=0)
    No.grid(row=1,column=1)
    popups.mainloop()

if __name__=="__main__":
 popups('George is the greatest person on the earth')
