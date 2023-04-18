#!/usr/bin/python3
"""Defining a class (Robot)"""


class Robot:
    """Representing a class Robot"""

    def __init__(self, name=None, built_year=None):
        """Initialization
        Args:
            name(str): The name of the Robot
            built_year(int): The manufacturing year
        """
        self.name = name
        self.built_year = built_year
    
    """Defining a greetings method"""
    def greetings(self):
        if self.name:
            print("Hello, my name is", self.name)
        else:
            print("I'm a nameless Bot")
            
        if self.built_year:
            print("I was built in", self.built_year)
        else:
            print("I don't know when I was created")

    """Defining set name met""" 
    def set_name(self, name):
        self.name = name
    """Defining get name"""
    def get_name(self):
        return self.name
    """Defining set built year"""
    def set_built_year(self, by):
        self.built_year =by
    """Defining get year method"""
    def get_built_year(self):
        return self.built_year
x = Robot("Mkelvo", 1923)
y = Robot()
y.set_name("Prince 1001 ")
x.greetings()
y.greetings()

















