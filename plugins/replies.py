from talk1.talk1 import talk


def replies(order):

    match order.lower():
        case "how are you":
            talk("I am fine, thank you.")
        case "what is your name":
            talk("My name is Elsa")
        case "what is your purpose":
            talk("My purpose is to help you")
        case "what is your favorite color":
            talk("My favorite color is green")
        case "what is your favorite food":
            talk("My favorite food is pizza.")
        case "what is your favorite sport":
            talk("My favorite sport is soccer.")
        case "what is your favorite movie":
            talk("My favorite movie is Frozen.")
        case "what is your favorite song":
            talk("My favorite song is Thousand Nights by Christina Perri.")
        case "what is your favorite book":
            talk("My favorite book is The Harry Potter.")
        case "what is your favorite game":
            talk("My favorite game is Minecraft.")
        case "what is your favorite animal":
            talk("My favorite animal is a dog.")


plugin_loader = (("how", replies), ("what", replies))

if __name__ == "__main__":
    while True:
        replies(input("What do you want to ask? "))
