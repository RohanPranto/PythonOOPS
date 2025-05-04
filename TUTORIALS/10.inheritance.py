# Base class or Parent class
class Vehicle:
    def __init__(self, brand, model, year):
        # Common attributes for all vehicles
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print("Bhroom Bhroom 💨💨💨")
        print(f"{self.__class__.__name__} is stopping 🏳️🏳️🏳️")  # Shows class name (Car or Bike)

    def stop(self):
        print("Peep Peep!!🏳️🏳️🏳️")
        print(f"{self.__class__.__name__} is stopping 🏳️🏳️🏳️")  # Shows class name


# Child class Car inherits from Vehicle
class Car(Vehicle):
    def __init__(self, brand, model, year, doors, wheels):
        super().__init__(brand, model, year)  # Call parent constructor to initialize brand, model, year
        self.doors = doors  # Additional attribute specific to Car
        self.wheels = wheels  # Additional attribute specific to Car


# Child class Bike also inherits from Vehicle
class Bike(Vehicle):
    def __init__(self, brand, model, year, wheels):
        super().__init__(brand, model, year)  # Reuse parent constructor
        self.wheels = wheels  # Bike-specific attribute


# Creating a Car object using the Car class (which uses Vehicle as base)
car = Car("Ferrari", "250 GTO", 1962, 2, 4)

# Creating a Bike object
bike = Bike("Yamaha", "R15", 2008, 2)

# __dict__ prints all attributes of the object in dictionary form
print(car.__dict__)
print(bike.__dict__)

# Calling any method inherited from Vehicle
bike.stop()
