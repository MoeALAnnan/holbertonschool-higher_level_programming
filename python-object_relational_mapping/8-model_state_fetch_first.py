#!/usr/bin/python3
"""Script that prints the first State object from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    # Get MySQL credentials
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    mysql_db = sys.argv[3]

    # Set up connection to MySQL server
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            mysql_user, mysql_password, mysql_db),
        pool_pre_ping=True)

    # Create session factory bound to the engine
    Session = sessionmaker(bind=engine)

    # Create a session and query for the first state object
    session = Session()
    state = session.query(State).order_by(State.id).first()

    # Print the first state object or "Not found" if there are no states
    if state:
        print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")
