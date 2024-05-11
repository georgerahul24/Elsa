import os
from pynput.keyboard import Key, Controller
from pynput import keyboard as KB
import pyautogui as pag
import webbrowser
from time import sleep
import pyscreeze


def on_press(key):
    return False





def send_mail(recipient, subject, body):
    keyboard = Controller()
    webbrowser.open("https://mail.google.com/mail/u/0/#inbox?compose=new", new=1, autoraise=True)

    with KB.Listener(
            on_press=on_press,
    ) as listener:
        listener.join()

    keyboard.type(recipient)
    sleep(0.3)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    sleep(0.3)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    sleep(0.3)
    keyboard.type(subject)
    sleep(0.3)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    sleep(0.3)
    keyboard.type(body)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)


send_mail("test@gmail.com", "Test Email", "Test")
