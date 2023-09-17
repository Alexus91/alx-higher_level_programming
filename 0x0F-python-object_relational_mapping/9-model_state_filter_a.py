#!/usr/bin/python3
"""
list all State objects that contain the letter a from a database
"""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                                    argv[2],
                                                                    argv[3]))
    Base.metadata.create_all(eng)
    Sess = sessionmaker(bind=eng)
    sess = Session()
    sym = '%a%'
    states = sess.query(State).filter(State.name.like(sym)).order_by(State.id)
    for state in states:
        print("{}: {}".format(state.id, state.name))
    sess.close()
