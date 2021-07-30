from tkinter import *
import add_user
import about_page
from talk1 import *

def setting_page():  
    a=Tk()    
    def usr_page(event=''):
        talk('Please add a new user')
        add_user.user_page()  
    def abt_page():
        talk('Here is the about page')
        about_page.about_page()

                 
    adduser=Button(a,text="Add User", command=usr_page )
    adduser.pack()
    about=Button(a,text="About",command=abt_page)
    about.pack()
    a.mainloop()

 