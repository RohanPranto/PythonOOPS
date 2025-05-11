num = int(input("Enter a number : "))
num_str = str(num)
digits = []
for d in num_str:
    digits.append(int(d))

length = len(digits)

total = 0
for i in range(length):
    total += digits[i] ** (i + 1) 

if total == num:
    print(num, "is a Disarium number.")
else:
    print(num, "is not a Disarium number.")
