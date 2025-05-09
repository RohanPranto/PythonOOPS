# Input number of vegetables
n = int(input())

# Initialize empty list to store vegetables
vegetables = []

# Input vegetable details and store in the list
for _ in range(n):
    name = input()
    price = float(input())
    quantity = int(input())
    vegetables.append([name, price, quantity])

# Input store name
store_name = input()

# Input minimum and maximum price range
min_price = float(input())
max_price = float(input())

# Categorize vegetables alphabetically
categorized_vegetables = {}
for veg in vegetables:
    first_letter = veg[0][0].lower()  # Get the first letter of vegetable name
    if first_letter not in categorized_vegetables:
        categorized_vegetables[first_letter] = []
    categorized_vegetables[first_letter].append(veg[0])

# Print categorized vegetables
for letter in sorted(categorized_vegetables.keys()):
    categorized_vegetables[letter].sort()  # Sort vegetable names
    print(letter)
    for vegetable in categorized_vegetables[letter]:
        print(vegetable)

# Filter vegetables within the price range
filtered_vegetables = []
for veg in vegetables:
    if min_price <= veg[1] <= max_price:
        filtered_vegetables.append(veg[0])

# Print filtered vegetables or message if none found
if filtered_vegetables:
    print(f"{min_price}-{max_price}")
    for vegetable in sorted(filtered_vegetables):
        print(vegetable)
else:
    print("No Vegetable(s) in the given price range")
