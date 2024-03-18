#!/usr/bin/python3

"""
Script that displays all values in the states table of hbtn_0e_0_usa
where name matches the provided argument.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    if len(argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(
            argv[0]))
        exit()

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(
            argv[4])
    cursor.execute(query)

    states = cursor.fetchall()

    for state in states:
        if state[1] == argv[4]:
            print(state)

    cursor.close()
    db.close()
