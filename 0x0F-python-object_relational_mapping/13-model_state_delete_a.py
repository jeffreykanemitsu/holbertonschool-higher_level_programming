#!/usr/bin/python3
'''
deletes all State objects with a name containing the letter a
from the database hbtn_0e_6_usa
'''

if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    from sqlalchemy import update
    ngin = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                                     argv[2],
                                                                     argv[3]))
    Base.metadata.create_all(ngin)
    Session = sessionmaker(bind=ngin)
    session = Session()
    for state in session.query(State).all():
        if 'a' in state.name:
            session.delete(state)
    session.commit()
