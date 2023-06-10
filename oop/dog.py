#!/usr/bin/python3
class Dog:
    def __init__(self, name="", age=0, weight=0):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        print("{} can bark".format(self.name))

    def eat(self):
        print("{} can eat".format(self.name))


spot = Dog("spot", 24, 35)
spot.bark()