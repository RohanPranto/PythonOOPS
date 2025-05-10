s = input("Enter a string: ")
upper_str = ""

for char in s:
    if 'a' <= char <= 'z':
        upper_str += chr(ord(char) - 32)
    else:
        upper_str += char

print("Uppercase:", upper_str)


#It works by subtracting 32 from the ASCII value of lowercase letters to get their uppercase equivalents.