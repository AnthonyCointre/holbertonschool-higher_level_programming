#!/usr/bin/python3
"""
List all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa.
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
        SELECT *
        FROM states
        ORDER BY states.id ASC
        """
    )
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
