#!/usr/bin/python3
"""
Take in an argument and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
import sys


def main():
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )
    cursor = db.cursor()
    query = (
        "SELECT * FROM states WHERE BINARY name = '{}' ORDER BY id ASC;"
        .format(state_name)
    )
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
