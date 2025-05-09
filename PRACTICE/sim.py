n = int(input())  # Number of SIMs
sim = []

# Reading SIM details
for i in range(n):
    simId = int(input())
    customerName = input()
    balance = float(input())
    ratePerSecond = float(input())
    circle = input()
    # Storing SIM details as a tuple
    sim.append([simId, customerName, balance, ratePerSecond, circle])

# Reading the old and new circles
circle1 = input()
circle2 = input()

# Finding SIMs with the given old circle and transferring them to the new circle
transferred = []

for i in sim:
    if i[4].lower() == circle1.lower():  # Case insensitive comparison
        transferred.append([i[0], i[1], circle2, i[3]])

# Sorting the transferred list by ratePerSecond in descending order
transferred.sort(key=lambda x: x[3], reverse=True)

# Outputting the transferred SIMs
if transferred:
    for t in transferred:
        print(f"{t[0]} {t[1]} {t[2]} {t[3]}")
else:
    print("No customers to transfer")
