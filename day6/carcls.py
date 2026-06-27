class Vehicle:
    def start(self):
        print("Vehicle started")

class Car(Vehicle):
    def start(self):
        print("Car started")

v=Vehicle()
c=Car()
v.start()
c.start()
