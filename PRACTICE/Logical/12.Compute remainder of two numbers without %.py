num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

while num1 >= num2:
    num1 -= num2

print("Remainder:", num1)
