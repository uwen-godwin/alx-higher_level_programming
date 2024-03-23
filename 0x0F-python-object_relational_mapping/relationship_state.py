#!/usr/bin/python3
"""Defines the State class."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """Represents a state for a MySQL database."""

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete-orphan")

    def __init__(self, name):
        """Initializes a new State.

        Args:
            name (str): The name of the state.
        """
        self.name = name
