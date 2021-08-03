from tkinter import *
from talk1 import *
import file_database


def user_page():
    s = Tk()
    lu = Label(s, text="Enter the username:")
    lp = Label(s, text="Enter the password:")
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
            talk("user aldready exists Try again")
            s.destroy()

    add_user_layout()
    add_user_button = Button(s, text="Add User", bd=0, command=add)
    add_user_button.grid(row=3, column=1)
    s.bind("<Return>", add)
    s.mainloop()


if __name__ == '__main__':
    user_page()
