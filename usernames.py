'''Created by George Rahul
Calls the login page and verifies the username and password entered'''

from GUI import SecurityUI
from talk1 import *
import file_database


def verify_usernames():
    verify_usernames.verify = False


def check_user():
    try:
        # initialise the security variable
        check_user.security = verify_usernames.verify
        # .....accept the username and password.......
        talk("Please enter the username and password")
        # ...running GUI.py............
        username, password = SecurityUI()
        # verifying with database
        passw = file_database.check_user_from_file(username)

        if password == passw:
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
