'''Created by George Rahul
Contains all the necessary code to run various features'''
import pyttsx3
import datetime
import subprocess
import webbrowser
from pathlib import Path
import os
from talk1 import talk
nam = "George"


#rewrite the entire pyttsxe using the talk from talk1 to simplify the code


usr = "USER"





# .....Time and Greeting............
def greeting():
    try:
        x = datetime.datetime.now().hour

        if x < 12:
            talk(f"Good morning {nam}")
        else:
            talk(f"Good evening {nam}")
    except:
        print("Sorry i couldnt do what you requested Try again later")


def tell_time():
    talk(f"It is {datetime.datetime.now().hour} hours")


# ...........Programmes..........................
def wordpad():
    try:
        subprocess.Popen('C:\\Windows\\System32\\write.exe')
        talk(f"I have opened wordpad for you  {nam}")
    except:
        print("Sorry i couldnt do what you requested Try again later")


def whatsapp():
    try:
        
        subprocess.Popen(f'C:\\Users\\{usr}\\AppData\\Local\\WhatsApp\\WhatsApp.exe')
        print("Opened WhatsApp")
        talk("I have opened whatsapp for you", nam)
        
    except:
        print("Sorry i couldnt do what you requested Try again later")






def gimp():
    try:
        subprocess.Popen("C:\\Program Files\\GIMP 2\\bin\\gimp-2.10.exe")
        talk("I have opened gimp for you")
    except:
        talk("Sorry i could not open gimp ")


def firefox():
    try:        
        subprocess.Popen('C:\\Program Files\\Mozilla Firefox\\firefox.exe')
        talk("i have opened firefox for you")
    except Exception as e:
        talk("Sorry, could not open firefox")
        print("Sorry i couldnt do what you requested Try again later",e)


# .........browser and net related................
def web(a):
    try:
        searchword = a
        webbrowser.open('https://www.google.com/search?client=firefox-b-d&q=' + searchword, new=1)
        
        talk("This is what I found for" + a)


        '''# webbrowser.open(searchword)
       # def google(a):
       # searchword  = a
       # url = []
       # for i in search(searchword,lang="en",num=10,start=1,stop=10,pause=2):
       # url.append(i)
       # print(i)
       # print(url)
       # engine.say("These are the links I Found for Your Search")
       # engine.runAndWait()'''
    except:
        webbrowser.open(webbrowser.open(searchword, new=1))
        print("Sorry i couldnt do what you requested Try again later")


def youtube(srch):
    webbrowser.open(f"https://www.youtube.com/results?search_query={srch}")
    talk(f"Here is what I found about {srch}")


# .............folders......................





def download():
    try:
       os.startfile(Path(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Downloads')))
       talk(f"Here is what you requested   {nam}")
    except:
        talk("Sorry, could not open the downloads folder")
        print("Sorry i couldnt do what you requested Try again later")
