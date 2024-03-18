#!/usr/bin/python3

"""
Script that displays all values in the states table of hbtn_0e_0_usa
where name matches the provided argument, and is AFE from MySQL injection.
Parameters for script: mysql username, mysql password, database name
and state name searched.
Must use the `MySQLdb` module.
Script should connect to a MySQL server runnimg on `localhost` at port `3306`
Must use `format` to create the SQL query with the user input.
Results must be in ascending order by `states.id`.
Code should not be executed when imported.
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

    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (argv[4],))

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()
