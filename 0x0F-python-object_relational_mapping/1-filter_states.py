#!/usr/bin/python3

"""
Script lists all states with a name starting with N from database
Connects to default host (localhost) and port (3306)
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db_user = sys.argv[1]

    db_password = sys.argv[2]

    db_name = sys.argv[3]

    
    db = MySQLdb.connect(user=db_user, passwd=db_password, db=db_name, host="localhost")

    c = db.cursor()

    c.execute("SELECT * FROM states "
                "WHERE name LIKE BINARY 'N%' " 
                "ORDER BY states.id ASC"
                )

    rows = c.fetchall()

    for row in rows:
        print(row)
    c.close()
    db.close()
