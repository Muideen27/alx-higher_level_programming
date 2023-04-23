#!/usr/bin/python3

'''
Write a script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.

'''
import MySQLdb
from sys import argv

if __name__ == '__main__':

    db = MySQLdb.connect(host="localhost", 
                            user=argv[1], 
                            passwd=argv[2], 
                            db=argv[3], 
                            port=3306
                        )
    
    with db.cursor() as c:
        c.execute("SELECT * FROM states WHERE name LIKE BINARY %(name)s "
                   "ORDER BY states.id ASC ", {'name': argv[4]})

    rows = c.fetchall()

    if rows is not None:
        for row in rows:
            print(row)
