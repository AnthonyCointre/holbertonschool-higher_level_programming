#!/usr/bin/python3
"""
Print all City objects from the database hbtn_0e_14_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

def main():
    if len(sys.argv) != 4:
        print("Usage: python 14-model_city_fetch_by_state.py <mysql_username> <mysql_password> <database_name>")
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Database connection
    engine = create_engine(f"mysql+mysqldb://{mysql_username}:{mysql_password}@localhost:3306/{database_name}")

    # Bind the Base class to the engine
    Base.metadata.bind = engine

    # Create session
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    # Query all cities, join with states, and order by city id
    cities = session.query(City).join(State).order_by(City.id).all()

    # Print results in the required format
    for city in cities:
        print(f'{city.state.name}: ({city.id}) {city.name}')

    session.close()

if __name__ == '__main__':
    main()
