import theme

bg_colour, text_color, button_colour = theme.read_theme()

def tkinter_initialise(a,x,y,top=1):
    a.withdraw()
    a.attributes("-alpha", 0.9)
    a.overrideredirect(True)
    a.configure(bg=bg_colour)
    a.resizable(0, 0)
    try:
        a.iconbitmap(r'icon.ico')

    except:
        print("Sorry i couldnt open the icon..")

    a.attributes("-topmost", top)
    a.title("Vira Version 1.1")
    a.geometry(f"+{x}+{y}")

    a.deiconify()  # show the tkinter window back


def on_enter(event,but):
        but.config(bg=button_colour)
def on_leave(event,but):
        but.config(bg=bg_colour)