#!/usr/bin/python3
"""class Rectangle which implements Base."""
from models.base import Base


class Rectangle(Base):
    """ class Rectangle implements Base."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the instance of the class."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Returns: width"""
        return self.__width

    @width.setter
    def width(self, value):
        """ setter function for width."""
        self.validate_int("width", value, False)
        self.__width = value

    @property
    def height(self):
        """Returns: height """
        return self.__height

    @height.setter
    def height(self, value):
        """setter function for height"""
        self.validate_int("height", value, False)
        self.__height = value

    @property
    def x(self):
        """Returns: x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter function for x."""
        self.validate_int("x", value)
        self.__x = value

    @property
    def y(self):
        """Returns: y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter function for y"""
        self.validate_int("y", value)
        self.__y = value

    def validate_integer(self, name, value, eq=True):
        '''Method for validating the value.'''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if eq and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not eq and value <= 0:
            raise ValueError("{} must be > 0".format(name))
