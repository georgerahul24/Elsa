from tkinter import *
import theme
import tkinterlib
from functools import partial

def about_page():
    bg_colour, text_color, button_colour = theme.read_theme()
    ab = Tk()
    tkinterlib.tkinter_initialise(ab,640,340)


    h = Label(ab, text="Created by:", bg=bg_colour,fg=text_color, font="bold").pack()
    g = Label(ab, text="Austin Bert",  bg=bg_colour,fg=text_color).pack()
    a = Label(ab, text="George Rahul", bg=bg_colour,fg=text_color).pack()
    e = Label(ab, text="Elizabeth Jaison",  bg=bg_colour,fg=text_color).pack()

    #img=PhotoImage(file='close_button.png')
    #ex=Button(ab,text="close",command=close_window,image=img).pack()

    ex = Button(ab,
                text="X",
                font="bold",
                bg=bg_colour, fg=text_color,
                command=ab.destroy,
                bd=0)
    ex.pack()

    ex.bind('<Enter>', partial(tkinterlib.on_enter, but=ex))
    ex.bind('<Leave>', partial(tkinterlib.on_leave, but=ex))

    ab.mainloop()


if __name__ == '__main__':
    about_page()
    print('Complete')
