#!/usr/bin/python3
"""
Contain the class definition of a State and
an instance Base = declarative_base().
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sys

Base = declarative_base()


class State(Base):
    """
    A class State that links to the MySQL table states.
    """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)


def main():
    if len(sys.argv) != 4:
        print("""
              Usage:./model_state.py <mysql username>
              <mysql password> <database name>
              """
              )
        sys.exit(1)
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost/{db_name}',
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)
