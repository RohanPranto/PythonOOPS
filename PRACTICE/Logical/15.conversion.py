# Decimal number
num = int(input("Enter a decimal number: "))

# Binary Conversion
binary = bin(num)[2:]  # bin() returns a string starting with '0b', so we slice it off
print("Binary:", binary)

# Octal Conversion
octal = oct(num)[2:]   # oct() returns a string starting with '0o', so we slice it off
print("Octal:", octal)

# Hexadecimal Conversion
hexadecimal = hex(num)[2:].upper()  # hex() returns a string starting with '0x', so we slice it off
print("Hexadecimal:", hexadecimal)
