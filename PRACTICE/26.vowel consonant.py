s = input("Enter a string: ").lower()

vowels = 0
consonants = 0

for char in s:
    if char.isalpha():
        if char in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
