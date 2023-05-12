class Robot:
    __counter = 0
    def __init__(self):
        type(self).__counter += 1
    def RobotInstance(self):
        return Robot.__counter

if __name__ == "__main__":
    x = Robot()
    print(x.RobotInstance())
    y = Robot()
    print(x.RobotInstance())