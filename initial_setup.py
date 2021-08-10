def install_files():
    f = open('initial.vira', 'w')
    f.write(
        "black;purple;light green \n #The order is bg,font color,button colour \n#Please remember to use ';' to separate colours :D"
    )
    f.close()
    f = open('users.vira', 'w')
    f.write("admin-1234")
    f.close()
    print("added file 'initial.vira'")


if __name__ == "__main__":
    install_files()
