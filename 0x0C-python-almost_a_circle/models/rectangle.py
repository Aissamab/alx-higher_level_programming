#!/usr/bin/python3
"""Defines a class Rectangle that inherits from Base"""


class Rectangle(Base):
    """Class that defines properties of Rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Creates new instances of a rectangle
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y

     @property
    def width(self):
        """Width of this rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Property setter for width of rectangle."""
        self.__width = value

    @property
    def height(self):
        """Height of rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Property setter for height of rectangle."""
        self.__height = value

    @property
    def x(self):
        """x retriever.

        """
        return self.__x

    @x.setter
    def x(self, value):
        """Property setter for x."""
        self.__x = value

    @property
    def y(self):
        """y retriever.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """the stter property for y"""
        self.__y = value
