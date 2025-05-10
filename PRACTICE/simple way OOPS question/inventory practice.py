inventories = []

for _ in range(4):
    id = int(input())
    maxQuantity = int(input())
    maxCurrent = int(input())
    threshold = int(input())

    inventories.append([id, maxQuantity, maxCurrent, threshold])

limit_threshold = int(input())

for inventory in inventories:
    if inventory[3] <= limit_threshold:
        if inventory[3] >= 75:
            print(f"{inventory[0]} Critical Filling")
        elif 50 <= inventory[3] < 75:
            print(f"{inventory[0]} Moderate Filling")
        else:
            print(f"{inventory[0]} Non critical filling")