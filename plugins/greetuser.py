username = 'gr'


def greetuser(afterword):
    print("Hello, " + username.title() + "!")


plugin_loader = (('abcd', greetuser),)
