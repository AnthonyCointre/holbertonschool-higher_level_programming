#!/usr/bin/python3
"""
List all cities from the database hbtn_0e_4_usa.
"""

import MySQLdb
from sys import argv


def main():
    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name,
        charset="utf8"
    )
    cur = conn.cursor()
    cur.execute(
        """
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
        """
    )
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
