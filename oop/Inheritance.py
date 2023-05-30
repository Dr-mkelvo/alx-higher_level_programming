"""Base class"""
class Animal:
    def eat(self):
        print("I eat everytime")

    def sleep(self):
        print("I sleep daily")

"""Child class"""
class Dog(Animal):
    def bark(self):
        print("I bark loudly")
   
"""Creating Objects"""
dog1 = Dog()
"""Calling members of the base/derived class"""
dog1.eat()
dog1.bark()
