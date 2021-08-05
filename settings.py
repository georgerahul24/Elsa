import random
from functools import partial
from tkinter import *
import add_user
import about_page
import tkinterlib
from talk1 import *
import history
import theme


def setting_page(username='', state=True):
    a = Tk()

    bg_colour, text_color, button_colour = theme.read_theme()

    tkinterlib.tkinter_initialise(a, 400, 340, top=0)

    def usr_page(event=''):
        talk('Please add a new user')
        add_user.user_page()

    def abt_page():
        talk('Here is the about page')
        about_page.about_page()

    #Learn abt partial methods here: https://www.geeksforgeeks.org/partial-functions-python/(used to partial arguments.Rest will be given by python itself)

    adduser = Button(a,
                     text="Add User",
                     bd=0,
                     command=usr_page,
                     bg=bg_colour,
                     fg=text_color)
    adduser.pack(fill='x')
    adduser.bind('<Enter>', partial(tkinterlib.on_enter, but=adduser))
    adduser.bind('<Leave>', partial(tkinterlib.on_leave, but=adduser))
    about = Button(a,
                   text="About",
                   command=abt_page,
                   bd=0,
                   bg=bg_colour,
                   fg=text_color)
    about.pack(fill='x')
    about.bind('<Enter>', partial(tkinterlib.on_enter, but=about))
    about.bind('<Leave>', partial(tkinterlib.on_leave, but=about))
    if state == True:
        showhis = Button(a,
                         text="Show History",
                         bd=0,
                         bg=bg_colour,
                         fg=text_color,
                         command=lambda: history.user_read(username))
        showhis.pack(fill='x')

        showhis.bind('<Enter>', partial(tkinterlib.on_enter, but=showhis))
        showhis.bind('<Leave>', partial(tkinterlib.on_leave, but=showhis))
        clearhis = Button(a,
                          text="Clear History",
                          bd=0,
                          bg=bg_colour,
                          fg=text_color,
                          command=lambda: history.clear_history(username))
        clearhis.pack(fill='x')

        clearhis.bind('<Enter>', partial(tkinterlib.on_enter, but=clearhis))
        clearhis.bind('<Leave>', partial(tkinterlib.on_leave, but=clearhis))

    close = Button(a,
                   text="x",
                   font='bold',
                   bd=0,
                   bg=bg_colour,
                   fg=text_color,
                   command=a.destroy)
    close.pack()

    close.bind('<Enter>', partial(tkinterlib.on_enter, but=close))
    close.bind('<Leave>', partial(tkinterlib.on_leave, but=close))

    a.mainloop()


if __name__ == "__main__":
    setting_page()
