#!/usr/bin/python3

"""
This script takes three command-line arguments and lists all State objects
from a MySQL database using SQLAlchemy.
"""

import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State


def main():
    """Main function."""

    # Check for correct number of arguments
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        return

    # Set up database connection
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query database and print results
    results = session.query(State).order_by(State.id)
    for row in results:
        print("{}: {}".format(row.id, row.name))


if __name__ == "__main__":
    main()
