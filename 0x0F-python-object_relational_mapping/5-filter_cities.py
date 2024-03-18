#!/usr/bin/python3

"""
Script that takes in the name of a state as an argument and lists all
cities of that state, using the database hbtn_0e_4_usa.
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

    city_query = """SELECT cities.name
                    FROM states
                    INNER JOIN cities ON states.id = cities.state_id
                    WHERE states.name = %s
                    ORDER BY cities.id ASC"""
    cursor.execute(city_query, (argv[4],))

    cities = cursor.fetchall()

    city_names = [city[0] for city in cities]
    print(", ".join(city_names))

