# 1st way: Accessing and modifying attributes directly

from datetime import datetime
class User:
    def __init__(self, username, email, password):  
        self.username = username          
        self._email = email   # Using a single underscore to indicate it's intended for internal use and not part of the public API     
        self.password = password      
    
    def get_email(self):
        return self._email.lower().strip() #GETTERS method to access the email attribute
    print("Email accessed at:", datetime.now())  
    
    def set_email(self, new_email):
        if "@" in new_email and "." in new_email:
            self._email = new_email.lower().strip()

user1 = User("Rohan", "  rohanROhan@gmail.com  ", "password123")

print(user1.get_email())  

user1.set_email("NewEmail@gmail.com")
print(user1.get_email())  # This will print the new assigned email.