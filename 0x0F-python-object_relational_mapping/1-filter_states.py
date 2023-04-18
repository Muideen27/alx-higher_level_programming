#!/usr/bin/python3
"""
Write a script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa

"""
import MySQLdb
import sys
"""
Taking argument and connecting to MyQSL server, it executes the SELECT command to retreive rows form states and sort in ascending order
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
    cur.execute("SELECT * FROM states\ WHERE name LIKE 'N%'\ ORDER BY id ASC"
    state = cur.fetchall()

    for row in state:
        print(row)
