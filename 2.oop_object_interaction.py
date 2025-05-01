# Define a class called User (A class is a blueprint for creating user objects)
class User:
    def __init__(self, username, email):  # Constructor (__init__) initializes the object with username and email
        self.username = username          # Instance variable to store the username
        self.email = email                # Instance variable to store the email address
    
    def say_hi(self, user):               # Method that takes another User object and prints a greeting
        print(f"Hey {user.username}, my name is {self.username}")
    
# Create the first user object with username "Rohan" and email "rohan24@gmail.com"
user1 = User("Rohan", "rohan24@gmail.com")

# Create the second user object with username "Bob" and email "Bobthe@gmail.com"
user2 = User("Bob", "Bobthe@gmail.com")

# Call the say_hi method from user1, passing user2 as an argument
user1.say_hi(user2)  # This will make user1 greet user2

'''
✅ What’s happening:
    User → class (blueprint)
    user1, user2 → objects/instances
    __init__ → constructor initializing data
    say_hi() → method showing interaction between two objects (user1 greeting user2)
'''