# Define a class called Person (Class is a blueprint for creating objects)
class Person:
    def __init__(self, name, age):  # This is the constructor (__init__ method); it runs automatically when an object is created
        self.name = name            # 'self.name' is an instance variable to store the name of the person
        self.age = age              # 'self.age' is an instance variable to store the age of the person
        
    def greet(self):                # This is a method (function inside a class) that allows the object to perform an action
        print(f"I am {self.name} and my age is {self.age}")  # Uses the object's data to print a greeting
        
# Create an object (instance) of the Person class with name "Rohan" and age 24
person1 = Person("Rohan", 24)  # 'person1' is an object; it has its own 'name' and 'age' stored inside

# Call the greet method on the object; this makes 'person1' introduce itself
person1.greet()

'''
🔍 OOP concepts explained here:
    ✅ Class → Person: blueprint for creating person objects
    ✅ Object → person1: actual instance created from the class
    ✅ Constructor → __init__: initializes the object with data
    ✅ Attributes → self.name, self.age: store object-specific data
    ✅ Method → greet: a function tied to the object's behavior
'''