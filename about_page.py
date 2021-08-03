from tkinter import *


def about_page():
    ab = Tk()
    ab.withdraw()
    ab.overrideredirect(True)  # remove borders
    ab.attributes("-alpha", 0.8)
    ab.configure(bg="light green")
    ab.attributes("-topmost", 1)
    ab.title("Vira Version 1.1")
    ab.resizable(0, 0)
    ab.geometry("+600+340")

    ab.deiconify()  # show the tkinter window back

    def close_window():
        ab.destroy()

    h = Label(ab, text="Created by:", bg="light green", font="bold").pack()
    g = Label(ab, text="Austin Bert", bg="light green").pack()
    a = Label(ab, text="George Rahul", bg="light green").pack()
    e = Label(ab, text="Elizabeth Jaison", bg="light green").pack()
    #img=PhotoImage(file='close_button.png')
    #ex=Button(ab,text="close",command=close_window,image=img).pack()
    ex = Button(ab,
                text="X",
                font="bold",
                bg="green",
                command=close_window,
                bd=1).pack()
    ab.mainloop()


if __name__ == '__main__':
    about_page()
    print('Complete')
