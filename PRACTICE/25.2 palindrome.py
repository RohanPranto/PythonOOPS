def is_palindrome(s):
    return s == s[::-1]

# Example usage
word = input("Enter a string: ")

if is_palindrome(word):
    print("Palindrome")
else:
    print("Not a palindrome")
