#!/usr/bin/python3
'''
prints the State object with the name passed as argument
from the database hbtn_0e_6_usa
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
    state = session.query(State.id).filter(State.name == argv[4]).all()
    if state:
        for row in state:
            print("{:d}".format(row[0]))
    else:
        print("Not found")
    session.close()
