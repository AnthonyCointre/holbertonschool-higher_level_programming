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
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    cities = session.query(City).join(State).order_by(City.id).all()
    for city in cities:
        print(f'{city.state.name}: ({city.id}) {city.name}')
    session.close()


if __name__ == '__main__':
    main()
