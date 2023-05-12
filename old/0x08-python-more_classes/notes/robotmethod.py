#!/usr/bin/python3
"""Defining a class Robot"""


class Robot:
    """Representing a class Robot"""
    def __init__(self, name=None):
        """ Initialization
        Args:
            name(str): Name of the robot -Set to none
        """
        self.name = name
    """Creating a method (greetings)"""
    def greetings(self):
        if self.name:
            print("Hey", self.name)
        else:
            print("I'm a nameless Robot")

"""Creating an Object"""
x = Robot()
x.greetings()
y = Robot("Mkelvo")
y.greetings()