'''Created by George Rahul
GUI for the login page'''

from tkinter import *
# Created by George Rahul
def SecurityUI():
    #.................initialising tkinter........................
    t = Tk()
    t.geometry("1x1")
    t.iconbitmap(r'icon.ico')
    t.withdraw()
    # t.deiconify() to make it appear again
    win = Toplevel(t)
    win.title("Vira Ver 1.1")
    win.resizable(0, 0)
    win.geometry("200x100+700+300")
    win.config(bg="light green")
    win.attributes("-topmost", 1)
    win.attributes("-alpha",0.8)
    win.iconbitmap(r'icon.ico')
    # win.overrideredirect(1)
    #........entry fileds for username and password.............
    e = Entry(win, show="*", width=10)
    e.place(x=104, y=30)
    e1 = Entry(win, width=10)
    e1.place(x=104, y=10)

    #..........Labels for username and password............................................
    t1 = Label(win, text="Username:", bg="light green", font="Nebula 10 bold").place(x=20, y=10)
    t2 = Label(win, text="Password:", bg="light green", font="Nebula 10 bold").place(x=20, y=30)

    win1 = Toplevel(t)
    win1.withdraw()
    win1.lift()
    #win1.attributes("-topmost", 1)



    def password(event):
        password.passgui = e.get()
        password.usergui = e1.get()





    def button(a):

        b = Button(win, text=a,bd=0, command=lambda:password(""))
        b.place(x=90, y=60)


    button("Verify")
    t.mainloop()
    return password.usergui, password.passgui

if __name__=="__main__":
    a=SecurityUI()
    print(a)
