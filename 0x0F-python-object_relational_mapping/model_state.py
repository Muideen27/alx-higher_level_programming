#!/usr/bin/python3

"""
Write a python file that contains the class definition 
of a State and an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """
    Attributes:
    __tablename__ (str): Table name of class
    id(int): id state of the class
    name(str): state name of the class
    """

    __tablename__ = 'states'

    id = Column(Integer,primary_key=True)
    name = Column(String(128), nullable=False)
