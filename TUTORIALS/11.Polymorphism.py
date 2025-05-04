#Polymorphism means "many forms". It allows us to define a single interface for different data types. For example, you are a son in home, a student in school, and an employee in the office. You are the same person but you play different roles in different places. Similarly, polymorphism allows us to define a single interface for different data types.

class Car:
    def __init__(self, brand, model,year,doors):
        self.brand = brand
        self.model = model
        self.year = year
        self.doors = doors

    def start(self):
        print("The car is starting")

    def stop(self):
        print("The car is stopping")

class Bike:
    def __init__(self, brand, model,year):
        self.brand = brand
        self.model = model
        self.year = year

    def start_bike(self):
        print("The bike is starting")

    def stop_bike(self):
        print("The bike is stopping")

#creating list of vehicles to inspect
vehicles = [
    Car("Ford", "focus", 2008, 5),
    Bike("Yamaha","R15",2008)
]

#loop through the list of vehicles and call the start and stop methods
for vehicle in vehicles:
    if isinstance(vehicle, Car):
        print (f"Car: {vehicle.brand} {vehicle.model} {vehicle.year} {vehicle.doors}")
        vehicle.start()
        vehicle.stop()

    elif isinstance(vehicle, Bike):
        print (f"Bike: {vehicle.brand} {vehicle.model} {vehicle.year}")
        vehicle.start_bike()
        vehicle.stop_bike()

    else:
        print("Unknown vehicle type")