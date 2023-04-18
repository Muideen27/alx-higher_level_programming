#!/usr/bin/python3
"""
script that lists all states from the database hbtn_0e_0_usa
Muideen27
"""
import MySQLdb
from sys import argv


def print_states(username, password, db_name):
    db = MySQLdb.connect(host="localhost", user=username, passwd=password, db=db_name, port=3306, charset="utf8")

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    data = cur.fetchall()

    for row in data:
        print(row)

        cur.close()
        db.close()

if __name__ == "__main__":
    credentials = argv
    username = argv[1]
    passwd = argv[2]
    db_name = argv[3]
    print_states(username, passwd, db_name)
