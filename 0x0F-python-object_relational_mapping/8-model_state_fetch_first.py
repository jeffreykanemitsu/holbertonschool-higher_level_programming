#!/usr/bin/python3
'''
lists all State objects from the database hbtn_0e_6_usa
'''

if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    ngin = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                                     argv[2],
                                                                     argv[3]))
    Base.metadata.create_all(ngin)
    Session = sessionmaker(bind=ngin)
    session = Session()
    state = session.query(State).order_by(State.id).first()
    if state:
        print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")
    session.close()
