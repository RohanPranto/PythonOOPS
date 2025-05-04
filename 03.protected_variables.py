# 1st way: Accessing and modifying attributes directly
class User:
    def __init__(self, username, email, password):  
        self.username = username          
        self._email = email   # Using a single underscore to indicate it's intended for internal use and not part of the public API     
        self.password = password      
    
    def clean_email(self):
        return self._email.lower().strip() #_email works inside the class but not outside the class
    
user1 = User("Rohan", "  rohanROhan@gmail.com  ", "password123")
print(user1._email)  # This will print the username
print(user1.clean_email())  # This will print the cleaned email address in lowercase and without leading/trailing spaces


'''
if we use double underscore, it will be name mangling and we cannot access the variable outside the class. for example:
_email is not name mangled, but __email is name mangled. _email can be accessed outside the class, but __email cannot be accessed outside the class.

we should not use any protected or private variables outside the class. we should use getter and setter methods to access and modify the variables outside the class.

🔍What is mangling? 
👉Name mangling is a technique used in Python to make class attributes private. It involves prefixing the attribute name with two underscores, which causes the interpreter to change the name of the attribute in a way that makes it harder to create subclasses that accidentally override the private attributes and methods.
'''