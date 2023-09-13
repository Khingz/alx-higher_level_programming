#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_city import City
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                sys.argv[1],
                sys.argv[2],
                sys.argv[3]),
            pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    for s, c in session.query(State, City)\
            .filter(State.id == City.state_id)\
            .all():
        print("{}: ({}) {}".format(s.name, c.id, c.name))
