#!/usr/bin/python3
"""
script that lists all states from the database hbtn_0e_0_usa
Muideen27
"""
import MySQLdb
import sys
"""
Taking arguments as input
"""
if __name__ == '__main__':
    username, password, database = sys.argv[1:]

    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            passwd=password,
            db=database
        )
    cur = db.cursor()

    cur.execute('SELECT * FROM states ORDER BY id ASC')

    for state in cur.fetchall():
        print(state)
