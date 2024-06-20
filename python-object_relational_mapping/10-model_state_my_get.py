#!/usr/bin/python3
"""
Print the State object with the name passed as argument
from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    if len(sys.argv) != 5:
        print("""
              Usage: {}
              <mysql username>
              <mysql password>
              <database name>
              <state name>
              """.format(sys.argv[0])
              )
        sys.exit(1)
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]
    engine = create_engine(
        f"mysql+mysqldb://{mysql_username}:{mysql_password}"
        f"@localhost:3306/{database_name}"
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).filter(State.name == state_name).first()
    if state:
        print(state.id)
    else:
        print("Not found")
    session.close()


if __name__ == "__main__":
    main()
