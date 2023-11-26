#!/usr/bin/python3
"""
This script takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name
matches the argument (safe from SQL injection).
"""

import sys
import MySQLdb

if __name__ == '__main__':
    # Retrieve arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=username, passwd=password, db=db_name)

    # Create cursor and execute query
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name=%s ORDER BY id ASC"
    cur.execute(query, (state_name,))

    # Retrieve results and print them out
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Close cursor and connection to database
    cur.close()
    db.close()
