#!/usr/bin/python3
"""
Add the State object “Louisiana” to the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    if len(sys.argv) != 4:
        print("""Usage: {} <mysql username>
              <mysql password>
              <database name>""".format(sys.argv[0])
              )
        sys.exit(1)
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    engine = create_engine(f'mysql+mysqldb: //
                           {mysql_username}:
                           {mysql_password}@localhost: 3306 /
                           {database_name}'
                           )
    Session = sessionmaker(bind=engine)
    session = Session()
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()
    print(new_state.id)
    session.close()


if __name__ == "__main__":
    main()
