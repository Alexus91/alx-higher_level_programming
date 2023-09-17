#!/usr/bin/python3
"""
prints the State object with the name passed as argument from a database
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    re = False
    for state in session.query(State):
        if state.name == sys.argv[4]:
            print('{}'.format(state.id))
            re = True
            break
    if re is False:
        print('Not found')
