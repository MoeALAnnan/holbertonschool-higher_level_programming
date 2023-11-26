#!/usr/bin/python3
"""List all the cities in a given state"""

import sys
import MySQLdb


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    cur = db.cursor()
    query = "SELECT GROUP_CONCAT(cities.name SEPARATOR ', ') FROM cities \
             JOIN states ON cities.state_id = states.id \
             WHERE states.name = %s"

    cur.execute(query, (state_name,))
    rows = cur.fetchall()
    if len(rows) == 0:
        print('')
    else:
        for row in rows:
            print(row[0] or '')
    cur.close()
    db.close()
