laptop = []

# Read 4 laptops
for i in range(4):
    laptopId = int(input())
    brand = input()
    osType = input()
    price = float(input())
    rating = int(input())
    laptop.append((laptopId, brand, osType, price, rating))

# Read brand and os to search
search_brand = input()
search_os = input()

# First: countOfLaptopsByBrand
brand_count = 0

for i in laptop:
    if i[1].lower() == search_brand.lower() and i[4] > 3:
        brand_count += 1

if brand_count > 0:
    print(brand_count)
else:
    print("The given brand is not available")

# Second: searchLaptopByOsType
matching_os = []

for i in laptop:
    if i[2].lower() == search_os.lower():
        matching_os.append(i)

if len(matching_os) == 0:
    print("The given os is not available")
else:
    # Sort by laptopId descending
    matching_os.sort(key=lambda x: x[0], reverse=True)
    for i in matching_os:
        print(i[0])
        print(i[4])
