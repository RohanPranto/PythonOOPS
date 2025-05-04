str=input("Enter a string: ").lower()

reversed=str[::-1]

if str==reversed:
    print("Palindrome")
else:
    print("Not palindrome")