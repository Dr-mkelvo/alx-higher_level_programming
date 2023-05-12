#!/usr/bin/python3
"""Defining a class (Square)"""


class Square:
    """Representing a class Square
    Attribute:
        __size (int): A private instance attribute
    """
    def __init__(self, size=0):
        """Initializing a square"""
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        
        self.__size = value


        
    """Representing a public instance attribute """
    def area(self):
        """Returning the area of the square"""

        return self.__size ** 2


    def my_print(self):
        """Printing the square """
        for x in range(0, self.__size):
            [print("#", end="") for y in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
