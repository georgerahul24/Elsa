import random,add_user,about_page,tkinterlib,history,theme
from functools import partial
from tkinter import *
from talk1 import talk




def setting_page(username='', state=True):
    settingspage = Tk()

    bg_colour, text_color, button_colour = theme.read_theme()

    tkinterlib.tkinter_initialise(settingspage, 400, 340, top=0)
    a = LabelFrame(settingspage, text="Settings", bg=bg_colour, fg=text_color)
    a.pack()

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

    change_theme = Button(a,
                   text="Change Theme",
                   command=theme.theme_selector,
                   bd=0,
                   bg=bg_colour,
                   fg=text_color)
    change_theme.pack(fill='x')
    change_theme.bind('<Enter>', partial(tkinterlib.on_enter, but=change_theme))
    change_theme.bind('<Leave>', partial(tkinterlib.on_leave, but=change_theme))



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

    close = Button(settingspage,
                   text="x",
                   font='bold',
                   bd=0,
                   bg=bg_colour,
                   fg=text_color,
                   command=settingspage.destroy)
    close.pack()

    close.bind('<Enter>', partial(tkinterlib.on_enter, but=close))
    close.bind('<Leave>', partial(tkinterlib.on_leave, but=close))

    settingspage.mainloop()


if __name__ == "__main__":
    setting_page()
