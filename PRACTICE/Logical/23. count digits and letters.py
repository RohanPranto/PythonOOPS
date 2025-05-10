def count_digits_and_letters(input_string):
    digits = 0
    letters = 0
    for char in input_string:
        if char.isdigit():
            digits += 1
        elif char.isalpha():
            letters += 1
    return digits, letters

# Input string from the user
input_string = input("Enter a string: ")

digits, letters = count_digits_and_letters(input_string)

print(f"Digits: {digits}")
print(f"Letters: {letters}")
