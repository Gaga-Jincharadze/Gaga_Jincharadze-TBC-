# Base class Vehicle
class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        print("The car is driving")

class Bike(Vehicle):
    def move(self):
        print("The bike is cycling")

class Truck(Vehicle):
    def move(self):
        print("The truck is hauling")

def test_vehicles(list):
    for vehicle in vehicles:
        vehicle.move()

car = Car()
bike = Bike()
truck = Truck()

vehicles = [car, bike, truck]
test_vehicles(vehicles)
