class Animals:
    def sleep(self):
        print("I love sleeping at night")

    def eat(self):
        print("I eat to live")

class Dog(Animals):
    def bark(self):
        print("Woof! Woof!")

d1 = Dog()
d1.bark()
d1.eat()
d1.sleep()