import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    user_email = Column(String(100), nullable=False)

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    character_name = Column(String(250), nullable=False)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    planet_name = Column(String(250))
    character_id = Column(Integer, ForeignKey('character.id'))
    character = relationship(Character)

class Starship(Base):
    __tablename__ = 'starship'
    id = Column(Integer, primary_key=True)
    starship_name = Column(String(250))
    character_id = Column(Integer, ForeignKey('character.id'))
    character = relationship(Character)

    def to_dict(self):
        return {}


render_er(Base, 'diagram.png')




