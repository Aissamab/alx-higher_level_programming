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
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Height of rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Property setter for height of rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x retriever.

        """
        return self.__x

    @x.setter
    def x(self, value):
        """Property setter for x."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value <= 0:
            raise ValueError("x must be > 0")
        self.__x = value

    @property
    def y(self):
        """y retriever.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """the stter property for y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value <= 0:
            raise ValueError("y must be > 0")
        self.__y = value

     def area(self):
        """Calculates the area of a rectangle.

        Returns:
            int: area.
        """
        return self.__width * self.__height
