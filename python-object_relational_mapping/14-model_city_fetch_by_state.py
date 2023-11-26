#!/usr/bin/python3
"""
similar to model_state.py named model_city.py
"""


import sys
from sqlalchemy.ext.declarative import declarative_base
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State, City).join(City).order_by(City.id).all()

    for state, city in result:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.commit()
    session.close()
