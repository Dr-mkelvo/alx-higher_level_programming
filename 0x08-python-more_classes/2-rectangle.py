#!/usr/bin/python3
"""Rectangle class defination."""


class Rectangle:
    """ This is a representation of a rectangle"""

    def __init__(self, width = 0, height = 0) :
        """Intitializing a new Rectangle
        
        Arguments:
            @width: Rectangle's integral width
            @height: Rectangle's integral height
        """
        
        self.width = width
        self.height = height

    """"""
    @property
    def width(self):
        """setting Rectangle's width '__' for 'hidding it'."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """setting the Rectangle's height."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the Rectangle's area."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the  Rectangle's perimeter."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
