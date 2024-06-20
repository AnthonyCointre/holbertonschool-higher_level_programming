#!/usr/bin/python3
"""
print the first State object from the database hbtn_0e_6_usa.
"""

from sys import argv
from model_state import Base, State
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
    state = session.query(State).order_by(State.id).first()
    if state:
        print(f"{state.id}: {state.name}")
    else:
        print("Nothing")
    session.close()


if __name__ == "__main__":
    main()
