from tkinter import *
def about_page():
    ab=Tk()
    h=Label(ab,text="Created by:").pack()
    g=Label(ab,text="Austin Bert").pack()
    a=Label(ab,text="George Rahul").pack()
    e=Label(ab,text="Elizabeth Jaison").pack()
    ab.mainloop()

if __name__=='__main__':
    about_page()
    print('Complete')