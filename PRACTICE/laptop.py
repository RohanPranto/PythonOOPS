# Reading the input
laptops = []

# Reading details for 4 laptops
for _ in range(4):
    laptopId = int(input())
    brand = input().strip()
    osType = input().strip()
    price = float(input())
    rating = int(input())
    # Storing the laptop data as a tuple (laptopId, brand, osType, price, rating)
    laptops.append((laptopId, brand, osType, price, rating))

# Reading the brand and OS for search
brand_search = input().strip()
os_search = input().strip()

# Implementing the countOfLaptopsByBrand method manually
count = 0
for laptop in laptops:
    if laptop[1].lower() == brand_search.lower() and laptop[4] > 3:
        count += 1

if count > 0:
    print(count)
else:
    print("The given brand is not available")

# Implementing the searchLaptopByOsType method manually
os_laptops = []
for laptop in laptops:
    if laptop[2].lower() == os_search.lower():
        os_laptops.append(laptop)

if os_laptops:
    os_laptops.sort(key=lambda x: x[0], reverse=True)  # Sorting by laptopId in descending order
    for laptop in os_laptops:
        print(f"{laptop[0]}\n{laptop[4]}")
else:
    print("The given os is not available")
