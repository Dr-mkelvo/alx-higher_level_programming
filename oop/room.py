class Room:
    length = 0.0
    width = 0.0

    def cal_area(self):
        print("The area of the room is ", self.length * self.width)

room1 = Room()
room1.length = 89
room1.width = 87

room1.cal_area()
