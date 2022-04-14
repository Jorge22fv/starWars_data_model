import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()


class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    planet_name = Column(String(250))
   
class Starship(Base):
    __tablename__ = 'starship'
    id = Column(Integer, primary_key=True)
    starship_name = Column(String(250))
   
class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    character_name = Column(String(250), nullable=False)
    planet_id = Column(Integer, ForeignKey('planet.id'))
    starship_id = Column( Integer, ForeignKey('starship.id'))
    planet = relationship(Planet)
    starship = relationship(Starship)

class Fav_character(Base):
    __tablename__ = 'fav_character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    character_id = Column(Integer, ForeignKey('character.id'))
    character = relationship(Character)
    
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    user_email = Column(String(100), nullable=False)
    fav_char = Column(Integer, ForeignKey('fav_character.id'))
    character =  relationship(Fav_character)

    def to_dict(self):
        return {}


render_er(Base, 'diagram.png')




