#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from models.place import Place
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import os


store = os.environ.get('HBNB_TYPE_STORAGE')

class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    if store == 'db':
        __tablename__ = 'cities'
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)

        # One city to many places
        places = relationship('Place', cascade='all, delete', backref='city')
    else:
        name = ''
