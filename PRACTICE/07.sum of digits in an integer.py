num = int(input("Enter your desired number: "))
sum_of_digits = 0

while num > 0:
    sum_of_digits += num % 10
    num //= 10

print(sum_of_digits)
