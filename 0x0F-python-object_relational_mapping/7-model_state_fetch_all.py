#!/usr/bin/python3

'''
Write a script that lists all State objects 
from the database hbtn_0e_6_usa
'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == '__main__':
    
    db_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(argv[1], argv[2], argv[3])
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    session = Session()

    for instance in session.query(State).order_by(State.id):
        print('{0}: {1}'.format(instance.id, instance.name))
