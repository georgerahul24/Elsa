from tkinter import *
import mysqlmake
from talk1 import *


def user_page():
   s=Tk()
   lu=Label(s,text="Enter the username:")
   lp=Label(s,text="Enter the password:")
   eu=Entry(s)
   ep=Entry(s)
   def add_user_layout():         
      lu.grid(row = 0, column = 0);eu.grid(row = 0, column = 1)
      lp.grid(row=1,column=0);ep.grid(row=1,column=1)
   def add(event=''):
      mysqlmake.makesql()
      try:
         new_user=eu.get()
         new_password=ep.get()
         mysqlmake.makesql.cur.execute(f"INSERT into usernames values('{new_user}','{new_password}') ")
         mysqlmake.makesql.con.commit()
         print(f"Aded user {new_user} ")         
         s.destroy()
         talk('Successfully added user')
      except:
         s.destroy
         talk("Sorry,the username is aldready taken. Please take a new one")
         user_page()
            

   
   add_user_layout()
   add_user_button=Button(s, text="Add User",bd=0, command=add)
   add_user_button.grid(row=3,column=1)
   s.bind("<Return>",add)
   s.mainloop()

if __name__=='__main__':
 user_page()   