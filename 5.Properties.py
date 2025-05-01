# 2nd way: using python properties
# Properties are a way to manage the access of class attributes in Python.

from datetime import datetime
class User:
    def __init__(self, username, email, password):  
        self.username = username          
        self._email = email      
        self.password = password      
   
    @property
    def email(self):
        print(f"Email accessed at {datetime.now()}")
        return self._email

user1 = User("Rohan", "rohan@gmail.com", "password123")
print(user1.email)  
