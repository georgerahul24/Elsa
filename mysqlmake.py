'''Created by George Rahul
This module integrates the mysql with the python and is used to check if the neccesary tables exists or not'''


import mysql.connector as my
def makesql():
    # passd=input("Please enter your MYSQL password: ")
    makesql.con = my.connect(host="localhost", user="root", password="1234")
    if makesql.con.is_connected() == True:
        print("Connected")

    else:
        print("Not connected")

    makesql.cur = makesql.con.cursor()
    makesql.cur.execute("Show databases")
    databases = makesql.cur.fetchall()
    if ('viraver2',) in databases:
        makesql.cur.execute("use viraver2")
        print("Database 'viraver2' exists, checking for table 'usernames'")
        makesql.cur.execute("show tables")
        tables = makesql.cur.fetchall()
        if ('usernames',) in tables:

            print("Table found")
            pass
        else:
            makesql.cur.execute("create table usernames(username varchar(100),passw varchar(100)) ")
            print("created table 'usernames'")
            makesql.cur.execute("insert into usernames values('admin','1234') ")
            makesql.con.commit()
            print("Added user admin")





    else:
        print("Creating database viraver2")
        makesql.cur.execute("create database viraver2")
        makesql.cur.execute("use viraver2")
        print("Database 'viraver2' created")
        makesql.cur.execute("create table usernames(username varchar(100),passw varchar(100)) ")
        print("created table 'usernames'")
        makesql.cur.execute("insert into usernames values('admin','1234') ")
        makesql.con.commit()
        print("Added user admin")


if __name__ == "__main__":
    makesql()
