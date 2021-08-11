import theme


def tkinter_initialise(a, x, y, top=1):
    bg_colour, text_color, button_colour = theme.read_theme()
    a.withdraw()  #Hide tkinter windows to finsih intialsa==zation
    a.attributes("-alpha", 0.9)  #Opacity of tkinter window
    a.overrideredirect(True)  #Remove Borders and default title bars
    a.configure(bg=bg_colour)
    a.attributes(
        "-topmost", top
    )  #Decides if the tkinter windows shld always be on the top of other window
    a.geometry(f"+{x}+{y}")  #positions tkinter windows at x and y coordinate

    a.deiconify()  # show the tkinter window back


def on_enter(event, but):
    #Change the button colour from background colour to button colour fo hover effect when mouse enters the button field
    bg_colour, text_color, button_colour = theme.read_theme()
    but.config(bg=button_colour)


def on_leave(event, but):
    # Change back the button colour to background colour when mouse leaves the button field.
    bg_colour, text_color, button_colour = theme.read_theme()
    but.config(bg=bg_colour)
