from talk1.talk1 import talk
from difflib import get_close_matches

# TODO: USe difflib and a list of replies to find the closest match
replies_dict = {"how are you": "I am fine, thank you", "what is your name": "My name is Elsa",
                "what is your purpose": "My purpose is to help you", "what is your favorite color": "My favorite color is green",
                "what is your favorite animal": "My favorite animal is a dog.", "what is your favorite book": "My favorite book is The Harry Potter.",
                "what is your favorite sport": "My favorite sport is soccer.", "what is your favorite movie": "My favorite movie is Frozen.",
                "what is your favorite song": "My favorite song is Thousand Nights by Christina Perri."}


def replies(order):
    closestmatch = get_close_matches(order.lower(), replies_dict.keys(), cutoff = 0.8, n = 1)
    talk(replies_dict[closestmatch[0]]) if len(closestmatch) > 0 else talk("Sorry. I couldnt understand what you meant")


plugin_loader = (("how", replies), ("what", replies))

if __name__ == "__main__":
    while True:
        replies(input("What do you want to ask? "))
