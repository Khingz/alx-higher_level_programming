#!/usr/bin/python3
"""class definition of a State
"""
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Class definition"""
    __tablename__ = 'states'

    id = Column(
            Integer,
            nullable=False,
            unique=True,
            autoincrement=True,
            primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship(
            "City",
            backref="state",
            cascade="all, delete-orphan")
