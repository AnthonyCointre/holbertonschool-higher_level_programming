#!/usr/bin/python3
"""
Take in arguments and displays all values in the states table of hbtn_0e_0_usa
where name matches the argument.
But this time, write one that is safe from MySQL injections
"""

import MySQLdb
from sys import argv


def main():
    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]
    state_name_searched = argv[4]
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
        WHERE name = %s
        ORDER BY states.id ASC
        """
        ,(state_name_searched)
    )
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
