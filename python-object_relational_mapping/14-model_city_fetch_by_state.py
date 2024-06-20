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
              <username>
              <password>
              <database_name>
              """.format(sys.argv[0])
              )
        sys.exit(1)
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine(
        """
        mysql+mysqldb://{}:{}@localhost:3306/{}
        """.format(username, password, db_name), pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(City).order_by(City.id).all()
    for city in cities:
        print("{}: ({}) {}".format(city.state.name, city.id, city.name))
    session.close()


if __name__ == "__main__":
    main()
