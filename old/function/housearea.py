class Room:
    length = 0
    width = 0
  
    
    def area(self):
        print("The area of the room is {}".format(self.length * self.width))

study_room = Room()
study_room.length = 5
study_room.width = 4
study_room.area()
