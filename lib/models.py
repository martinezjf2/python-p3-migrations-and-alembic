
#!/usr/bin/env python3
from datetime import datetime

from sqlalchemy import create_engine, desc
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///migrations_test.db')
Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer(), primary_key=True)
    name = Column(String(), index=True)
    email = Column(String(55))
    grade = Column(Integer())
    birthday = Column(DateTime(), default=datetime.now())
    enrolled_date = Column(DateTime(), default=datetime.now())
    
    def __repr__(self):
        return f"Student {self.id}: \n {self.name}, \n Grade: {self.grade}"
    
    
    # Create a lib folder and cd into it
    # Run alembic init migrations to create migrations environment
    # create models.py that will within the same directory as alembic.ini
    # To create migrations make sure you are within the lib folder and run this command: alembic revision --autogenerate -m 'Message here'
    # To update the migrations to be head run this command: alembic upgrade head