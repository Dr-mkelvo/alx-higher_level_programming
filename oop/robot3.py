class Robot:
    def __init__(self, name=None):
        self.name = name
    def say_hi(self):
        if self.name:
            print("Hello, I'm " + self.name)
        else:
            print("Hello, I'm a nameless robot")

x = Robot()
x.say_hi()
y = Robot("Mkelvo")
y.say_hi()