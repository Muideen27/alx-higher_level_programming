#!/usr/bin/python3
'''
Write a script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.

'''

import MySQLdb
import sys

if __name__ == '__main__':

    db_user = sys.argv[1]

    db_password = sys.argv[2]

    db_name = sys.argv[3]


    ''' connecting to database '''
    db = MySQL.connect(host="localhost", 
                        user=db_user, 
                        passwd=db_password, 
                        db=db_name
                   )

    c = db.cursor()

    c.execute("SELECT * FROM states WHERE name LIKE '{:s}' "
                    "ORDER BY id ASC".format(argv[4]))

    rows = c.fetchall()
    for row in rows:
        print(row)
