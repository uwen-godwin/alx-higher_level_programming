#!/usr/bin/python3
"""Script that creates the State “California” with the City “San Francisco”"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    # Create SQLAlchemy engine to connect to MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create all tables in the engine
    Base.metadata.create_all(engine)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Create a new State object
    new_state = State(name="California")

    # Create a new City object
    new_city = City(name="San Francisco", state=new_state)

    # Add objects to the session
    session.add(new_state)
    session.add(new_city)

    # Commit the transaction
    session.commit()

    # Close the session
    session.close()
