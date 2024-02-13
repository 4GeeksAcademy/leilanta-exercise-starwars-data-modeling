import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
Base = declarative_base()



class user(Base):
    __tablename__ = 'users'
    email = Column(Integer, primary_key=True)
    user = Column(String(250), ForeignKey('starships_favorites'),ForeignKey('characters_favorites'),ForeignKey('planets_favorites'))
    password = Column(String(250), nullable=False)


class Starships(Base):
    __tablename__ = 'starships'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250), nullable=False)
    type_of_starship = Column(String(250), nullable=False)
    cost_in_credits = Column(String(250), nullable=False)
    longitude = Column(String(250), nullable=False)
    passanger_capacity = Column(Integer, nullable=False)
    MGLT = Column(String(250), nullable=False)
    charge_capacity = Column(Integer, nullable=False)
    provisions = Column(Integer, nullable=False)
    hypermotor = Column(String(250), nullable=False)
class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    gender =Column(String(250), nullable=False)
    specie =Column(String(250), nullable=False)
    height =Column(String(250), nullable=False)
    mass=Column(String(250), nullable=False)
    skin_color =Column(String(250), nullable=False)
    eye_color =Column(String(250), nullable=False)
    birth_year =Column(String(250), nullable=False)
    hair_color =Column(String(250), nullable=False)
class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    terrain =Column(String(250), nullable=False)
    poblacion =Column(String(250), nullable=False)
    diameter =Column(String(250), nullable=False)
    rotation_period =Column(String(250), nullable=False)
    orbital_period =Column(String(250), nullable=False)
    gravity =Column(String(250), nullable=False)
    climate =Column(String(250), nullable=False)
    surface_water =Column(String(250), nullable=False)


class Starships_favorites(Base):
    __tablename__ = 'starships_favorites'
    id = Column(Integer, primary_key=True)
    starship_id = Column(Integer, ForeignKey('starships.id'))
    user_id =Column(Integer, ForeignKey('starships.id'))
class Characters_favorites(Base):
    __tablename__ = 'characters_favorites'
    id = Column(Integer, primary_key=True)
    starship_id = Column(Integer, ForeignKey('characters.id'))
    user_id =Column(Integer, ForeignKey('characters.id'))
class Planets_favorites(Base):
    __tablename__ = 'planets_favorites'
    id = Column(Integer, primary_key=True)
    starship_id = Column(Integer, ForeignKey('planets.id'))
    user_id =Column(Integer, ForeignKey('planets.id'))

 
    


    def to_dict(self):
        return {}
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
