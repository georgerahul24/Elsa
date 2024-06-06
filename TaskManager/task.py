import datetime
import webbrowser


def tell_time():
    return f"It is {datetime.datetime.now().hour} {datetime.datetime.now().minute}"


def web(a):
    searchword = a
    webbrowser.open("https://www.google.com/search?client=firefox-b-d&q=" +
                    searchword,
                    new=1)


def youtube(srch):
    webbrowser.open(f"https://www.youtube.com/results?search_query={srch}")


