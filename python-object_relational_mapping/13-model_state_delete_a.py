#!/usr/bin/python3
"""
deletes all State objects with a name containing the letter a
"""


import sys
from sqlalchemy.ext.declarative import declarative_base
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State).filter(
        State.name.ilike('%a%')).order_by(State.id)

    for i in result:
        session.delete(i)
    session.commit()
    session.close()
