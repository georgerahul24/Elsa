import datetime
import webbrowser


def user_file(username, command, task_did):
    history = open(f'{username}.vira', 'a')
    history.write(
        f'{datetime.datetime.now()} user input: {command}, output: {task_did}')
    history.write('\n')
    history.close()


def user_read(username):
    webbrowser.open(f"{username}.vira")


def clear_history(name):
    history = open(f'{name}.vira', 'w')
    history.write('')
    history.close()
