#!/usr/bin/python3

"""
Script that prints the State object with the name passed as argument
from the database hbtn_0e_6_usa.
"""

from sys import argv
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    if len(argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(
            argv[0]))
        exit()

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    state_name = argv[4]
    queried_state = session.query(State).filter(
        State.name == state_name).first()

    if queried_state:
        print("{:d}".format(queried_state.id))
    else:
        print("Not found")

    session.close()
