from tkinter import *


def read_theme():
    try:
        f = open("initial.elsa")
        datas = f.read()
        colours = datas.split(';')
        bg_colour = colours[0].rstrip().lstrip()
        text_color = colours[1].rstrip().lstrip()
        colours = colours[2].split('\n')

        button_colour = colours[0].rstrip().lstrip()
        return bg_colour, text_color, button_colour
    except Exception as e:
        print('initial.elsa is corrupted')
        print(e)


def theme_writer(bg_colour, font_colour, button_colour):
    f = open('initial.elsa', 'w')
    f.write(
        f"{bg_colour};{font_colour};{button_colour}\n #The order is bg,font color,button colour \n#Please remember to use ';' to separate colours :D"
    )
    f.close()


def theme_selector(event=''):
    from tkinter.colorchooser import askcolor
    import Magic.tkinterlib as tkinterlib
    from functools import partial
    import Magic.theme as theme

    bg_colour, text_color, button_colour = theme.read_theme()

    selectorpage = Tk()
    tkinterlib.tkinter_initialise(selectorpage, 600, 340, top=0)
    selector = LabelFrame(selectorpage,
                          text="Theme",
                          bg=bg_colour,
                          fg=text_color)
    selector.pack()

    def new_background_colour(event=''):
        color = askcolor()
        bg_colour, text_color, button_colour = theme.read_theme()
        if color[1] != None:
            theme_writer(color[1], text_color, button_colour)

    def font_colour(event=''):
        color = askcolor()
        bg_colour, text_color, button_colour = theme.read_theme()
        if color[1] != None:
            theme_writer(bg_colour, color[1], button_colour)

    def new_button_colour(event=''):
        color = askcolor()
        bg_colour, text_color, button_colour = theme.read_theme()
        if color[1] != None:
            theme_writer(bg_colour, text_color, color[1])

    background_colour = Button(selector,
                               text="Background Colour",
                               bd=0,
                               bg=bg_colour,
                               fg=text_color,
                               command=new_background_colour)
    background_colour.pack()
    background_colour.bind('<Enter>',
                           partial(tkinterlib.on_enter, but=background_colour))
    background_colour.bind('<Leave>',
                           partial(tkinterlib.on_leave, but=background_colour))

    new_text_colour = Button(selector,
                             text="Font Colour",
                             bd=0,
                             bg=bg_colour,
                             fg=text_color,
                             command=font_colour)
    new_text_colour.pack()
    new_text_colour.bind('<Enter>',
                         partial(tkinterlib.on_enter, but=new_text_colour))
    new_text_colour.bind('<Leave>',
                         partial(tkinterlib.on_leave, but=new_text_colour))

    new_button_colour = Button(selector,
                               text="Button color",
                               bd=0,
                               bg=bg_colour,
                               fg=text_color,
                               command=new_button_colour)
    new_button_colour.pack()
    new_button_colour.bind('<Enter>',
                           partial(tkinterlib.on_enter, but=new_button_colour))
    new_button_colour.bind('<Leave>',
                           partial(tkinterlib.on_leave, but=new_button_colour))

    close = Button(selectorpage,
                   text="x",
                   font='bold',
                   bd=0,
                   bg=bg_colour,
                   fg=text_color,
                   command=selectorpage.destroy)
    close.pack()

    close.bind('<Enter>', partial(tkinterlib.on_enter, but=close))
    close.bind('<Leave>', partial(tkinterlib.on_leave, but=close))
    selectorpage.mainloop()
