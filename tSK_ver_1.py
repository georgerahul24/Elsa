'''Created by George Rahul'''
import pyttsx3
import datetime
import subprocess
import webbrowser
from pathlib import Path
import os

nam = "George"
from googlesearch import search

engine = pyttsx3.init()

voices = engine.getProperty('voices')  # getting details of current voice
# engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)  # changing index, changes voices. 1 for female

rate = engine.getProperty('rate')  # getting details of current speaking rate
engine.setProperty('rate', 150)  # setting up new voice rate

global usr
usr = "USER"





# .....Time and Greeting............
def greeting():
    try:
        x = datetime.datetime.now().hour

        if x < 12:
            engine.say(f"Good morning {nam}")
            engine.runAndWait()
        else:
            engine.say(f"Good evening {nam}")
            engine.runAndWait()
    except:
        print("Sorry i couldnt do what you requested Try again later")


def tell_time():
    engine.say(f"It is {datetime.datetime.now().hour} hours")

    engine.runAndWait()


# ...........Programmes..........................
def wordpad():
    try:
        engine.say(f"I have opened wordpad for you  {nam}")
        engine.runAndWait()
        subprocess.Popen('C:\\Windows\\System32\\write.exe')
    except:
        print("Sorry i couldnt do what you requested Try again later")


def whatsapp():
    try:
        subprocess.Popen(f'C:\\Users\\{usr}\\AppData\\Local\\WhatsApp\\WhatsApp.exe')
        engine.say("I have opened whatsapp for you", nam)
        engine.runAndWait()
        print("Opened WhatsApp")
    except:
        print("Sorry i couldnt do what you requested Try again later")






def gimp():
    try:
        subprocess.Popen("C:\\Program Files\\GIMP 2\\bin\\gimp-2.10.exe")
        engine.say("I have opened gimp for you")
        engine.runAndWait()
    except:
        engine.say("Sorry i could not open gimp ")
        engine.runAndWait()


def firefox():
    try:
        engine.say(f"I have opened firefox for you  {nam}")
        engine.runAndWait()
        subprocess.Popen('C:\\Program Files\\Mozilla Firefox\\firefox.exe')
    except:
        print("Sorry i couldnt do what you requested Try again later")


# .........browser and net related................
def web(a):
    try:
        searchword = a
        webbrowser.open('https://www.google.com/search?client=firefox-b-d&q=' + searchword, new=1)
        engine.say("This is what I found for" + a)
        engine.runAndWait()
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
        print("Sorry i couldnt do what you requested Try again later")


def youtube(srch):
    webbrowser.open(f"https://www.youtube.com/results?search_query={srch}")
    engine.say(f"Here is what I found about {srch}")
    engine.runAndWait()


# .............folders......................





def download():
    try:
        engine.say(f"Here is what you requested   {nam}")
        engine.runAndWait()
        os.startfile(Path(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Downloads')))
    except:
        print("Sorry i couldnt do what you requested Try again later")

