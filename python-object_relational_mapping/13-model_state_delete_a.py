#!/usr/bin/python3
"""
Delete all State objects with a name containing the letter a
from the database hbtn_0e_6_usa.
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
    states_to_delete = session.query(
        State).filter(State.name.like('%a%')).all()
    for state in states_to_delete:
        session.delete(state)
    session.commit()
    session.close()


if __name__ == "__main__":
    main()
