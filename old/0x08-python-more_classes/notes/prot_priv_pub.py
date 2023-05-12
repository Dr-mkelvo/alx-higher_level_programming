#!/usr/bin/python3
"""Defining class robot"""


class Robot:
    """Representing class Robot"""

    def __init__(self, name=None, built_year=2000):
        """Initializing class
        Args:
            Name(str): The name of the Robot
            Built Year(int): Year of Robot creation
        """
        self.__name = name
        self.__built_year = built_year
    
    """Defining a method greetings"""
    def greetings(self):
        if self.__name:
            print("Hello, I'm ", self.__name)
        else:
            print("I'm a nameless Bot")

    def set_name(self, name):
        self.__name = name
    def get_name(self):
        return self.__name
    def set_built_year(self, by):
        self.__built_year = by
    def get_built_year(self):
        return self.__built_year
    def __repr__(self):
        return "Name: " + self.__name + ", Built Year, " + str(self.__built_year)
if __name__ == "__main__":
    x = Robot("Mkelvo", 1002)
    y = Robot("MKVG", 1003)
    for bot in [x, y]:
        bot.greetings()
        if bot.get_name() == "MKVG":
            bot.set_built_year(1003)
        print("I was built in the year: " + str(bot.get_built_year()) + "!")