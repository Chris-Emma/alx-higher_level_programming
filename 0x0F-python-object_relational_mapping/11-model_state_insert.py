#!/usr/bin/python3

"""
Script that adds the State object “Louisiana” to the database hbtn_0e_6_usa.
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

    new_state = State(name="Louisiana")

    session.add(new_state)
    session.commit()

    print("{}".format(new_state.id))

    session.close()
