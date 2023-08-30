#!/usr/bin/env python3

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'  # Specify the table name
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)  # Example additional column

if __name__ == '__main__':
    engine = create_engine('sqlite:///students.db')  # Adjust the database URL
    Base.metadata.create_all(engine)
