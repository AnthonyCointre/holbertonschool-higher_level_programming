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
        print("""
              Usage: {}
              <mysql username>
              <mysql password>
              <database name>
              """.format(sys.argv[0])
              )
        sys.exit(1)
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    engine = create_engine(
        f"mysql+mysqldb://{mysql_username}:{mysql_password}"
        f"@localhost:3306/{database_name}"
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(City, State).filter(City.state_id == State.id).all()
    for city, state in cities:
        print(f"{state.name}: ({city.id}) {city.name}")
    session.close()


if __name__ == "__main__":
    main()
