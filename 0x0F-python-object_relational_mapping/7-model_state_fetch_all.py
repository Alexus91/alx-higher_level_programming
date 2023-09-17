#!/usr/bin/python3
"""lists all State objects from the database 'hbtn_0e_6_usa'"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                                    argv[2],
                                                                    argv[3]))
    Base.metadata.create_all(engi)
    sess = sessionmaker(bind=engi)()
    for state in sess.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
    sess.close()
