class Robot:
    def __init__(self, name = None):
        self.name = name


    def say_hi(self):
        if self.name:
            print("Hello, my name is" + self.name)
        else:
            print("Hello, I'm a nameless Robot")


x = Robot()
x.say_hi()
y = Robot("Mkelvo")
y.say_hi()
