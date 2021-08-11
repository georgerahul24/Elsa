from tkinter import *
import theme
import tkinterlib
from functools import partial


def about_page():
    bg_colour, text_color, button_colour = theme.read_theme()
    aboutpage = Tk()

    tkinterlib.tkinter_initialise(aboutpage, 640, 340)
    version = LabelFrame(aboutpage,
                         text="Version",
                         bg=bg_colour,
                         fg=text_color)
    verlabel = Label(version, text="Vira 1.1.120", bg=bg_colour, fg=text_color)
    verlabel.pack()
    version.pack(fill="both")

    ab = LabelFrame(aboutpage, text="Created By", bg=bg_colour, fg=text_color)
    ab.pack()
    #Name labels
    a = Label(ab, text="Austin Bert", bg=bg_colour, fg=text_color).pack()
    e = Label(ab, text="Elizabeth Jaison", bg=bg_colour, fg=text_color).pack()
    g = Label(ab, text="George Rahul", bg=bg_colour, fg=text_color).pack()
    #exit button
    ex = Button(aboutpage,
                text="X",
                font="bold",
                bg=bg_colour,
                fg=text_color,
                command=aboutpage.destroy,
                bd=0)
    ex.pack()
    #hover effect
    ex.bind('<Enter>', partial(tkinterlib.on_enter, but=ex))
    ex.bind('<Leave>', partial(tkinterlib.on_leave, but=ex))

    aboutpage.mainloop()


if __name__ == '__main__':
    about_page()
