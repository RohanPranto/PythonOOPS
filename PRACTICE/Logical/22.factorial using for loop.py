def factorial(n):
    result = 1
    for i in range(1, n+1):  # Loop through numbers from 1 to n
        result *= i  # Multiply each number to the result
    return result

# Input number from the user
num = int(input("Enter a number: "))

print(f"The factorial of {num} is: {factorial(num)}")
