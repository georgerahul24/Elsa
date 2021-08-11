def install_files():
    #Writing the default theme
    f = open('initial.vira', 'w')
    f.write(
        "black;purple;light green\n#The order is bg,font color,button colour\n#Please remember to use ';' to separate colours :D"
    )
    f.close()

    #writing the users folder with default user admin and default password 1234
    f = open('users.vira', 'w')
    f.write("admin-1234")
    f.close()
    print("added file 'initial.vira'")


if __name__ == "__main__":
    install_files()
