from talk1 import talk
def check_user_from_file(username):
    try:
        file = open(f"users.vira", 'r')
        lines = file.read().splitlines()

        for line in lines:
            parts = line.split('-')
            part1 = parts[0]#username
            part2 = parts[1]#passwords
            if part1==username:
                break
        return part2
    except Exception as e: print(e)


def write_to_file(username,password):
    try:
            file=open("users.vira")
            lines=file.read().splitlines()
            count=0
            for line in lines:
                parts = line.split('-')
                part1 = parts[0]  # username
                part2 = parts[1]  # passwords
                if part1==username:
                    count+=1


            if count==0:
                file = open("users.vira", 'a')
                file.write(f"\n{username}-{password}")
                file.close()
                print(f"Added user {username} ")
                state=1

            else:
               print('User already exists')
               state=-1
            return state
    except Exception as e:print(e,'Try again')

