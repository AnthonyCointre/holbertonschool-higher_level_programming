#!/usr/bin/python3
"""
Change the name of a State object from the database hbtn_0e_6_usa.
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
    state = session.query(State).filter(State.id == 2).all()
    if state:
        state[0].name = "New Mexico"
    session.commit()
    session.close()


if __name__ == "__main__":
    main()
