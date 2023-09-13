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
    data = session.query(State).filter(State.id == 2).first()
    if data:
        data.name = 'New Mexico'
    session.commit()
