from sqlalchemy import Column, String, Integer, Date, Numeric, Text, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from base import Base
from planet import Planet

class Moon(Base):
    __tablename__ = 'moon'
    id_name = "moon_id"

    id = Column(id_name, Integer, primary_key=True)
    name = Column('name', String(100), nullable=False, unique=True)
    diameter = Column('diameter', Integer, nullable=False)
    mass = Column('mass', Integer, nullable=False)
    age_in_millions_of_years = Column('age_in_millions_of_years', Numeric)
    description = Column('description', Text)
    has_life = Column('has_life', Boolean)
    is_spherical = Column('is_spherical', Boolean)
    planet_id = Column(Planet.id_name, Integer, ForeignKey('planet.' + Planet.id_name))
    planet = relationship('Planet', backref='moon')

    def __init__(self, name, diameter, mass, age_in_millions_of_years, description, has_life, is_spherical, planet):
        self.name = name
        self.diameter = diameter
        self.mass = mass
        self.age_in_millions_of_years = age_in_millions_of_years
        self.description = description
        self.has_life = has_life
        self.is_spherical = is_spherical
        self.planet = planet
