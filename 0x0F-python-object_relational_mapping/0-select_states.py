#!/usr/bin/python3
"""
script that lists all states from the database hbtn_0e_0_usa
Muideen27

"""
import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(
                        user=sys.argv[1],
                        passwd=sys.argv[2],
                        db=sys.argv[3],
                        host='localhost',
                        port=3306
                    )

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    data = cur.fetchall()

    for row in data:
        print(row)

        cur.closet()
        db.close()
