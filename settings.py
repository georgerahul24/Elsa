from tkinter import *
import add_user
import about_page

def setting_page():  
    a=Tk()    
    def usr_page(event=''):
        add_user.user_page()  
    def abt_page():
        about_page.about_page()

                 
    adduser=Button(a,text="Add User", command=usr_page )
    adduser.pack()
    about=Button(a,text="About",command=abt_page)
    about.pack()
    a.mainloop()

 