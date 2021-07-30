from tkinter import *
import mysqlmake

s=Tk()
def settings_page():
   lu=Label(s,text="Enter the username:")
   lp=Label(s,text="Enter the password:")
   eu=Entry(s)
   ep=Entry(s)
   def add_user_layout():    
      
      lu.grid(row = 0, column = 0);eu.grid(row = 0, column = 1);
      lp.grid(row=1,column=0);ep.grid(row=1,column=1)
   def add(event=''):
      mysqlmake.makesql()
      new_user=eu.get()
      new_password=ep.get()
      mysqlmake.makesql.cur.execute(f"INSERT into usernames values('{new_user}','{new_password}') ")
      mysqlmake.makesql.con.commit()
      print(f"Aded user {new_user} ")
      s.destroy()

   
   add_user_layout()
   add_user_button=Button(s, text="Add User",bd=0, command=add)
   add_user_button.grid(row=3,column=1)
   s.mainloop()
settings_page()   