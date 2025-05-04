from datetime import datetime

# Define a class named 'User'
class User:
    def __init__(self, username, email, password):  
        # Public attribute (can be accessed directly)
        self.username = username

        # Protected attribute (by convention, should not be accessed directly outside the class)
        self._email = email

        # Public attribute
        self.password = password      

    # This is a getter method for the email attribute using the @property decorator
    @property
    def email(self):
        print(f"Email accessed at {datetime.now()}")
        return self._email

    # This is a setter method for email using the @<property_name>.setter decorator
    @email.setter
    def email(self, new_email):
        # Simple validation: only update if "@" is in the new email
        if "@" in new_email:
            self._email = new_email
        else:
            # If the condition fails, don't change the email (no error thrown)
            pass


# Create an instance of User
user1 = User("Rohan", "rohan@gmail.com", "password123")

# Try to set an invalid email (doesn't contain "@")
user1.email = "this is email"  # This will be ignored by the setter as it doesn't contain "@"

# Access and print the email. Getter is called, so time will be printed
print(user1.email)  # Output: rohan@gmail.com (original value, since invalid one was ignored)
