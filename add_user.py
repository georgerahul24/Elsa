from tkinter import *

import tkinterlib
from talk1 import *
import file_database
import theme
from functools import partial
def user_page():
    s = Tk()
    bg_colour, text_color, button_colour = theme.read_theme()
    tkinterlib.tkinter_initialise(s,600,340)
    def close_window():
        s.destroy()

    lu = Label(s, text="Enter the username:",bg=bg_colour,fg=text_color)
    lp = Label(s, text="Enter the password:",bg=bg_colour,fg=text_color)
    eu = Entry(s)
    ep = Entry(s)

    def add_user_layout():
        lu.grid(row=0, column=0)
        eu.grid(row=0, column=1)
        lp.grid(row=1, column=0)
        ep.grid(row=1, column=1)

    def add(event=''):

        new_user = eu.get()
        new_password = ep.get()
        state = file_database.write_to_file(new_user, new_password)
        if state == 1:
            talk(f'Successfully added {new_user}')
            s.destroy()
        elif state == -1:
            talk("user aldready exists. Try again")
            s.destroy()

    add_user_layout()
    add_user_button = Button(s,
                             text="Add User",

                             bd=0,
                             command=add,bg = bg_colour,fg=text_color
                             )
    add_user_button.grid(row=3, column=1)
    add_user_button.bind('<Enter>', partial(tkinterlib.on_enter, but=add_user_button))
    add_user_button.bind('<Leave>', partial(tkinterlib.on_leave, but=add_user_button))
    close_button = Button(s,
                          text="X",
                          font="Bold"
    , bg = bg_colour, fg = text_color,
                          command=s.destroy,
                          bd=0)

    close_button.grid(row=3, column=0)

    close_button.bind('<Enter>', partial(tkinterlib.on_enter, but=close_button))
    close_button.bind('<Leave>', partial(tkinterlib.on_leave, but=close_button))
    s.bind("<Return>", add)
    s.mainloop()


if __name__ == '__main__':
    user_page()
