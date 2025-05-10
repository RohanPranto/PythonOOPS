def demo_args_kwargs(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

# Example
demo_args_kwargs(1, 2, 3, name="Rohan", age=24)

# can you explain the above code in detail and also provide a similar example with a different function name and different parameters?
# what is args and kwargs in the above code?
# args and kwargs are used to pass a variable number of arguments to a function.
# args is a tuple that contains all the positional arguments passed to the function.    
# kwargs is a dictionary that contains all the keyword arguments passed to the function.
# In the example, demo_args_kwargs(1, 2, 3, name="Rohan", age=24), the function is called with three positional arguments (1, 2, 3) and two keyword arguments (name="Rohan", age=24).
# The function prints the positional arguments as a tuple and the keyword arguments as a dictionary.
