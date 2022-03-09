from datetime import datetime
from talk1.talk1 import talk


def time(order=None):
    currenttime=datetime.now().strftime("%I:%M").split(":")
    # using int(currenttime) to convert instances starting with 0 like -> 06 to 6
    talk(f"The current time is {int(currenttime[0])} {int(currenttime[1])} ")


plugin_loader = (('time', time),)
