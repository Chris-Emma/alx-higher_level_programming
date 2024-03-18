#!/usr/bin/python3

"""
Script that lists all State objects from the database hbtn_0e_6_usa.
"""

from sys import argv
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    if len(argv) != 4:
        print("Usage: {} <username> <password> <database>".format(argv[0]))
        exit()

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()

    for state in states:
        print("{:d}: {:s}".format(state.id, state.name))

    session.close()
