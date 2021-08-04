from tkinter import *
import add_user
import about_page
from talk1 import *
import history
import theme

def setting_page(username='', state=True):
    a = Tk()
    bg_colour, text_color, button_colour = theme.read_theme()
    a.withdraw()
    a.attributes("-alpha", 0.8)
    a.configure(bg=bg_colour)
    a.resizable(0,0)
    try:
        a.iconbitmap(r'icon.ico')

    except:
        print("Sorry i couldnt open the icon..")

    a.attributes("-topmost", 0)
    a.title("Vira Version 1.1")
    a.geometry("+400+340")

    a.deiconify()  # show the tkinter window back

    def usr_page(event=''):
        talk('Please add a new user')
        add_user.user_page()

    def abt_page():
        talk('Here is the about page')
        about_page.about_page()

    adduser = Button(a, text="Add User", command=usr_page ,bg=button_colour,fg=text_color)
    adduser.pack()
    about = Button(a, text="About", command=abt_page,bg=button_colour,fg=text_color)
    about.pack()
    if state == True:
        showhis = Button(a,
                         text="Show History",bg=button_colour,fg=text_color,
                         command=lambda: history.user_read(username)).pack()
        clearhis = Button(
            a,
            text="Clear History",bg=button_colour,fg=text_color,
            command=lambda: history.clear_history(username)).pack()
    about.pack()
    a.mainloop()


if __name__ == "__main__":
    setting_page()
