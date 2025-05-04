# FizzBuzz is a classic programming problem often used in interviews or as a beginner exercise.

# Problem Statement:
# Print numbers from 1 to N. But:

# If a number is divisible by 3, print "Fizz" instead.

# If divisible by 5, print "Buzz".

# If divisible by both 3 and 5, print "FizzBuzz".

# Otherwise, just print the number.

limit=int(input("Enter limit: "))

for i in range (1, limit+1):
    if i%3==0 and i%5!=0:
        print("Fizz")
    elif i%5==0 and i%3!=0:
        print ("Buzz")
    elif i%3==0 and i%5==0:
        print ("Fizzbuzz")
    else:
        print(i)