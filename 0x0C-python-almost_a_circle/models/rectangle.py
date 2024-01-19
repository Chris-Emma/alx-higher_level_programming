#!/usr/bin/python3
""" Defines a rectangle class."""
from models.base import Base

class Rectangle(Base):
    """This represents the rechtangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """This initializes the rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
