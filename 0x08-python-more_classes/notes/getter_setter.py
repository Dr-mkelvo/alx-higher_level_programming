#!/usr/bin/python3
"""Defining a class Robot"""


class Robot:
    """Represennting a class (Robot)"""
    def __init__(self, name=None):
        """Initialization
        Args:
            name(str): The name of the Robot
        """
        self.name = name
    """Defining a greetings method"""
    def greetings(self):
        if self.name:
            print("Hello", self.name)
        else:
            print("Hello, I'm a nameless Robot")
    """Defining setter Method (set_name)"""
    def set_name(self, name):
        self.name =name
    
    """Defining a getter Method (get_name)"""
    def get_name(self):
        return self.name

"""Creating an Object"""
x = Robot()
x.set_name("Mkelvo")
x.greetings()

"""Creating Object 2"""
y = Robot()
y.set_name(x.get_name())
print(y.get_name())