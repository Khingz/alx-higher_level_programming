#!/usr/bin/python3
"""lists all State objects from the database
"""
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__" and len(argv) == 4:
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                argv[1],
                argv[2],
                argv[3]),
            pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    (session.query(State)
            .filter(State.name.like('%a%'))
            .delete(synchronize_session='fetch'))
    session.commit()
