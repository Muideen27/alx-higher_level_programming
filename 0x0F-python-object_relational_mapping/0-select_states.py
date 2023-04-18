#!/usr/bin/python3
"""
script that lists all states from the database hbtn_0e_0_usa
Muideen27

"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
            passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("SELLECT * FROM states")
    rows = cur.fetchall()

    for row in rows:
        print(row)
