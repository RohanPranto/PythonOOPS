seconds = int(input("Enter seconds: "))

hours = seconds // 3600
minutes = (seconds % 3600) // 60
seconds = seconds % 60

print(f"{hours:02}:{minutes:02}:{seconds:02}") 
# :02 means 2 digits, so if the number is less than 10, it will be padded with a 0. which is, 2 will be 02, 5 will be 05, and so on.


