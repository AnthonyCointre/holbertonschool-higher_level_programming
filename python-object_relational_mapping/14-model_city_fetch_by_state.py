#!/usr/bin/python3
"""
Print all City objects from the database hbtn_0e_14_usa.
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


def main():
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}"
        .format(argv[1], argv[2], argv[3]), pool_pre_ping=True
    )
    Base.metadata.crate_all = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    cities = session.query(City, State).filter(City.state_id == State.id).all()
    for city, state in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.commit()
    session.close()


if __name__ == '__main__':
    main()
