def read_theme():
    try:
        f=open("initial.vira")
        datas=f.read()
        colours=datas.split(';')
        bg_colour=colours[0].rstrip().lstrip()
        text_color=colours[1].rstrip().lstrip()
        colours=colours[2].split('\n')

        button_colour=colours[0].rstrip().lstrip()
        return bg_colour,text_color,button_colour
    except Exception as e:
        print('initial.vira is corrupted')
        print(e)


if __name__ == "__main__":
    bg_colour, text_color, button_colour=read_theme()
    print(bg_colour,text_color,button_colour)