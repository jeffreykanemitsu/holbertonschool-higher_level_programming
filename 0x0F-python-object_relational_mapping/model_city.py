#!/usr/bin/python3
'''
Contains class definition of a City
'''

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import State, Base


class City(Base):
    '''
    defines City class
    '''
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
