from tkinter import *
import add_user
import about_page
from talk1 import *
import history


def setting_page(username='', state=True):
    a = Tk()

    def usr_page(event=''):
        talk('Please add a new user')
        add_user.user_page()

    def abt_page():
        talk('Here is the about page')
        about_page.about_page()

    adduser = Button(a, text="Add User", command=usr_page)
    adduser.pack()
    about = Button(a, text="About", command=abt_page)
    about.pack()
    if state == True:
        showhis = Button(a,
                         text="Show History",
                         command=lambda: history.user_read(username)).pack()
        clearhis = Button(
            a,
            text="Clear History",
            command=lambda: history.clear_history(username)).pack()
    about.pack()
    a.mainloop()


if __name__ == "__main__":
    setting_page()
