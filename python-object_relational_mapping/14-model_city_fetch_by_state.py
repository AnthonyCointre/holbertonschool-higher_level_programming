#!/usr/bin/python3
"""
Print all City objects from the database hbtn_0e_14_usa.
"""

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def main():
    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}"
        .format(mysql_username, mysql_password, database_name),
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(City, State).filter(City.state_id == State.id).all()
    for city, state in cities:
        print(f"{state.name}: ({city.id}) {city.name}")
    session.close()


if __name__ == "__main__":
    main()
