#!/usr/bin/python3
"""Defining a class."""


class Rectangle:
    """Methods creation"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialization

        Args:
            width: Rectangle's width.
            height: Rectangle's height.
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
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
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ("")

        my_rectangle = []
        for i in range(self.__height):
            [my_rectangle.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                my_rectangle.append("\n")
        return ("".join(my_rectangle))

    def __repr__(self):
        my_rectangle = "Rectangle(" + str(self.__width)
        my_rectangle += ", " + str(self.__height) + ")"
        return (my_rectangle)

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
