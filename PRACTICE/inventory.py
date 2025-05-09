# List to store inventories
inventories = []

# Read 4 inventories
for _ in range(4):
    inventory = {}
    inventory['inventoryId'] = input().strip()
    inventory['maximumQuantity'] = int(input())
    inventory['currentQuantity'] = int(input())
    inventory['threshold'] = int(input())
    inventories.append(inventory)

# Read the limit
limit = int(input())

# Apply the replenish logic
for inventory in inventories:
    if inventory['threshold'] <= limit:
        print(inventory['inventoryId'], end=' ')
        if inventory['threshold'] >= 75:
            print("Critical Filling")
        elif 50 <= inventory['threshold'] <= 74:
            print("Moderate Filling")
        else:
            print("Non-Critical Filling")
