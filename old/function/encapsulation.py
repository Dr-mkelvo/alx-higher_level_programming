"""This is the bundling of attributes and methods in a single class
It prevents outer classes from modifying and accessing the attributes and methods
"""

class Computer:
    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("The price of a computer is ${}".format(self.__maxprice))

    
    def setMax(self, price):
        self.__maxprice = price

c = Computer()
c.sell()
c.__maxprice = 1200
c.sell()

c.setMax(1992)
c.sell()

