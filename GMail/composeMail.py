
from pynput import keyboard as KB
import pyautogui as pag
import webbrowser
from time import sleep



def on_press(key):
    return False


def send_mail(recipient, subject, body):
    webbrowser.open("https://mail.google.com/mail/u/0/#inbox?compose=new", new=1, autoraise=True)

    with KB.Listener(
            on_press=on_press,
    ) as listener:
        listener.join()
    print("Got keystroke")
    # Selecting the recipient
    sleep(0.3)
    pag.write(recipient)
    sleep(0.5)
    pag.press('tab')
    pag.press('tab')
    print("Hi")
    # Writing the subject
    pag.write(subject)
    pag.press('tab')
    # Writing the body
    pag.write(body)
    # TODO: Try removing the last 'tab' then the email address is written again
    pag.press('tab')
    return


if __name__ == "__main__":
    send_mail("georgerahul24@gmail.com", "Test Email", "Test")
    