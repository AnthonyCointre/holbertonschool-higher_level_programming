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
              <mysql_username>
              <mysql_password>
              <database_name>
              """.format(sys.argv[0])
              )
        sys.exit(1)
    
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    
    # Database connection
    engine = create_engine(
        f"mysql+mysqldb://{mysql_username}:{mysql_password}"
        f"@localhost:3306/{database_name}"
    )
    
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Query cities joined with states and ordered by city id
    cities = session.query(City).join(State).order_by(City.id).all()
    
    # Print results in the required format
    for city in cities:
        print(f'{city.state.name}: ({city.id}) {city.name}')
    
    session.close()

if __name__ == '__main__':
    main()
