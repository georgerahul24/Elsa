'''Created by George Rahul
Calls the login page and verifies the username and password entered'''

from GUI import SecurityUI
from talk1 import *

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
        talk("Please enter the username and password")
        # ...running GUI.py............
        username, password = SecurityUI()
        # verifying with database
        mysqlmake.makesql.cur.execute(
            f"select passw from usernames where username='{username}' ")
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
