import os
import sys
from sqlalchemy.orm import declarative_base, Mapped, mapped_column
from sqlalchemy import create_engine, ForeignKey
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False)

class Character(Base):
    __tablename__ = 'character'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    birth_year: Mapped[int] = mapped_column(nullable=False)
    gender: Mapped[str] = mapped_column(nullable=False)
    height: Mapped[int] = mapped_column(nullable=False)
    mass: Mapped[int] = mapped_column(nullable=False)
    skin_color: Mapped[str] = mapped_column(nullable=False)
    eye_color: Mapped[str] = mapped_column(nullable=False)
    hair_color: Mapped[str] = mapped_column(nullable=False)
    species: Mapped[str] = mapped_column(nullable=False)
    vehicle: Mapped[str] = mapped_column(ForeignKey("vehicle.id"))
    home_planet: Mapped[str] = mapped_column(ForeignKey("planet.id"))
    starship: Mapped[int] = mapped_column(ForeignKey("starship.id"))

class Planet(Base):
    __tablename__ = 'planet'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    climate: Mapped[str] = mapped_column(nullable=False)
    population: Mapped[int] = mapped_column(nullable=False)
    surface_water: Mapped[int] = mapped_column(nullable=False)
    orbital_period: Mapped[int] = mapped_column(nullable=False)
    rotation_period: Mapped[int] = mapped_column(nullable=False)
    diameter: Mapped[int] = mapped_column(nullable=False)
    gravity: Mapped[str] = mapped_column(nullable=False)
    terrain: Mapped[str] = mapped_column(nullable=False)
    residents: Mapped[int] = mapped_column(ForeignKey("character.id"))

class Vehicle(Base):
    __tablename__ = 'vehicle'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    model: Mapped[str] = mapped_column(nullable=False)
    manufacturer: Mapped[str] = mapped_column(nullable=False)
    cost: Mapped[int] = mapped_column(nullable=False)
    vehicle_class: Mapped[str] = mapped_column(nullable=False)
    consumables: Mapped[str] = mapped_column(nullable=False)
    length: Mapped[int] = mapped_column(nullable=False)
    speed: Mapped[int] = mapped_column(nullable=False)
    passengers: Mapped[int] = mapped_column(nullable=False)
    crew: Mapped[int] = mapped_column(nullable=False)
    cargo_capacity: Mapped[int] = mapped_column(nullable=False)
    consumables: Mapped[str] = mapped_column(nullable=False)
    pilot: Mapped[int] = mapped_column(ForeignKey("character.id"))

    
class Starship(Base):
    __tablename__ = 'starship'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    model: Mapped[str] = mapped_column(nullable=False)
    manufacturer: Mapped[str] = mapped_column(nullable=False)
    cost: Mapped[int] = mapped_column(nullable=False)
    vehicle_class: Mapped[str] = mapped_column(nullable=False)
    consumables: Mapped[str] = mapped_column(nullable=False)
    length: Mapped[int] = mapped_column(nullable=False)
    speed: Mapped[int] = mapped_column(nullable=False)
    passengers: Mapped[int] = mapped_column(nullable=False)
    crew: Mapped[int] = mapped_column(nullable=False)
    cargo_capacity: Mapped[int] = mapped_column(nullable=False)
    consumables: Mapped[str] = mapped_column(nullable=False)
    hyperdrive_rating: Mapped[int] = mapped_column(nullable=False)
    mglt: Mapped[int] = mapped_column(nullable=False)
    pilot: Mapped[int] = mapped_column(ForeignKey("character.id"))

class Favorite(Base):
    __tablename__ = 'favorite'
    id: Mapped[int] = mapped_column(primary_key=True)
    favorite_character: Mapped[int] = mapped_column(ForeignKey("character.id"), nullable=True)
    favorite_planet: Mapped[int] = mapped_column(ForeignKey("planet.id"), nullable=True)
    favorite_vehicle: Mapped[int] = mapped_column(ForeignKey("vehicle.id"), nullable=True)
    favorite_starship: Mapped[int] = mapped_column(ForeignKey("starship.id"), nullable=True)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
