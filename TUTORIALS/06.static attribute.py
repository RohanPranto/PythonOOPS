#static attribute is an attribute that is shared by all instances of a class and belongs to the class itself, not to any specific instance.

class User:
    user_count = 0 # This is a static attribute and is shared by all instances of the class

    def __init__(self, username, email):
        self.username= username
        self.email= email
        User.user_count +=1

    def display_user(self):
        print(f"Username: {self.username}, Email:{self.email}")

user1 = User("Rohan", "rohan@gmail.com")
user2 = User("Shrestha", "Shrestha@gmail.com")
user3 = User("Pranto", "Pranto@gmail.com")

print(f"total user: {User.user_count}")
print(f"total user: {user1.user_count}")
#both works because user_count is static and will be shared with every instances of the class