import theme

bg_colour, text_color, button_colour = theme.read_theme()


def tkinter_initialise(a, x, y, top=1):
    a.withdraw()#Hide tkinter windows to finsih intialsa==zation
    a.attributes("-alpha", 0.9)
    a.overrideredirect(True)
    a.configure(bg=bg_colour) 
    a.attributes("-topmost", top)    
    a.geometry(f"+{x}+{y}")

    a.deiconify()  # show the tkinter window back

def on_enter(event, but):
    
    but.config(bg=button_colour)

def on_leave(event, but):
    
    but.config(bg=bg_colour)
