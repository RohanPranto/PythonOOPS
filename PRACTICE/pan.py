# Reading the input for pan objects
n = int(input())

# List to store the pan objects
pans = []

# Reading 7 pan objects
for _ in range(n):
    pan = {}
    pan['id'] = input()
    pan['material'] = input()
    pan['brand'] = input()
    pan['price'] = int(input())
    pan['capacity'] = int(input())
    pans.append(pan)

# Function to find the costliest pan of a given material
def costliest_pan(pans, material):
    max_price = -1
    costliest = None
    for pan in pans:
        if pan['material'] == material and pan['price'] > max_price:
            max_price = pan['price']
            costliest = pan
    return costliest

# Function to calculate discounted price based on capacity
def discounted_price(pans, brand):
    for pan in pans:
        if pan['brand'] == brand:
            if pan['capacity'] > 1000:
                pan['price'] = int(pan['price'] * 0.74)  # 26% discount
            elif pan['capacity'] > 500:
                pan['price'] = int(pan['price'] * 0.80)  # 20% discount
            return pan['price']
    return None

# Input material and brand to search for
material = input()
brand = input()

# Find and print the costliest pan for the given material
costliest = costliest_pan(pans, material)
if costliest:
    print(costliest['id'])
else:
    print("No pan found for the material")

# Calculate and print the discounted price for the given brand
discounted = discounted_price(pans, brand)
if discounted is not None:
    print(discounted)
else:
    print("No pan found for the brand")
