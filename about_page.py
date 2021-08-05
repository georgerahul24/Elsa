from tkinter import *
import theme


def about_page():
    bg_colour, text_color, button_colour = theme.read_theme()
    ab = Tk()
    ab.withdraw()
    ab.overrideredirect(True)  # remove borders
    ab.attributes("-alpha", 0.8)
    ab.configure(bg=bg_colour)
    ab.attributes("-topmost", 1)
    ab.title("Vira Version 1.1")
    ab.resizable(0, 0)
    ab.geometry("+600+340")

    ab.deiconify()  # show the tkinter window back

    def close_window():
        ab.destroy()

    h = Label(ab, text="Created by:", bg=bg_colour, fg=text_color,
              font="bold").pack()
    g = Label(ab, text="Austin Bert", bg=bg_colour, fg=text_color).pack()
    a = Label(ab, text="George Rahul", bg=bg_colour, fg=text_color).pack()
    e = Label(ab, text="Elizabeth Jaison", bg=bg_colour, fg=text_color).pack()
    #img=PhotoImage(file='close_button.png')
    #ex=Button(ab,text="close",command=close_window,image=img).pack()
    ex = Button(ab,
                text="X",
                font="bold",
                bg=button_colour,
                fg=text_color,
                command=close_window,
                bd=1).pack()
    ab.mainloop()


if __name__ == '__main__':
    about_page()
    print('Complete')
