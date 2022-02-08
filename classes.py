class Building():
    def __init__(self, type, floors, price):
        self.type = type
        self.floors = floors
        self.price = price

    def describe_building(self):
        print("The building is a " + self.type + " with " + str(self.floors) +\
        " floors and it costs $" + str(self.price) + "." )

class Hotel(Building):
    def __init__(self, type, name, price, rooms):
        super().__init__(type, name, price)
        self.rooms = rooms

    def show_rooms(self):
        print(self.rooms)

    def update_rooms(self, rooms):
        self.rooms = rooms

    def has_auditorium(self):
        if self.rooms > 20:
            print("Yes")
        else:
            print("No")


shop = Building("shop", 1, 2000)
shop.describe_building()

suncity = Hotel("hotel", "4", 250000, 19)
suncity.describe_building()
suncity.has_auditorium()
suncity.show_rooms()
suncity.update_rooms(23)
suncity.has_auditorium()