from tkinter import *
from talk1 import *
import file_database


def user_page():
    s = Tk()
    s.withdraw()
    s.attributes("-alpha", 0.8)
    s.configure(bg="light blue")
    s.overrideredirect(True)
    try:
        s.iconbitmap(r'icon.ico')

    except:
        print("Sorry i couldnt open the icon..")

    s.attributes("-topmost", 1)
    s.title("Vira Version 1.1")
    s.geometry("+600+340")

    s.deiconify()  # show the tkinter window back

    def close_window():
        s.destroy()

    lu = Label(s, text="Enter the username:", bg="light blue")
    lp = Label(s, text="Enter the password:", bg="light blue")
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
    add_user_button = Button(s,
                             text="Add User",
                             fg="black",
                             bd=2,
                             command=add,
                             bg="light blue")
    add_user_button.grid(row=3, column=1)
    close_button = Button(s,
                          text="X",
                          font="Bold",
                          bg="light blue",
                          command=close_window,
                          bd=0).grid(row=3, column=0)
    s.bind("<Return>", add)
    s.mainloop()


if __name__ == '__main__':
    user_page()
