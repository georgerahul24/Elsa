'''Created by George Rahul'''
import pyttsx3
from GUI import SecurityUI

engine = pyttsx3.init()
voices = engine.getProperty('voices')  # getting details of current voice
# engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)  # changing index, changes voices. 1 for female
rate = engine.getProperty('rate')  # getting details of current speaking rate
engine.setProperty('rate', 130)  # setting up new voice rate
try:
    import mysqlmake

    mysqlmake.makesql()
except:
    print("Could not connect with database")


def verify_usernames():
    verify_usernames.verify = False


def check_user():
    try:
        # initialise the security variable
        check_user.security = verify_usernames.verify
        # .....accept the username and password.......
        engine.say("Please enter the username and password")
        engine.runAndWait()
        # ...running GUI.py............
        username, password = SecurityUI()
        # username = password.usergui
        # password =  password.passgui
        # database
        mysqlmake.makesql.cur.execute(f"select passw from usernames where username='{username}' ")
        passw = mysqlmake.makesql.cur.fetchall()

        if password == passw[0][0]:
            check_user.security = True

            pass
        else:
            check_user.security = False

        check_user.loginname = username

    except Exception as e:
        print(e)
        check_user.security = False


if __name__ == "__main__":
    verify_usernames()
    check_user()
