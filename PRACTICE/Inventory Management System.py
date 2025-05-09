class Inventory:
    def __init__(self, inventoryId, maximumQuantity, currentQuantity, threshold):
        self.inventoryId = inventoryId
        self.maximumQuantity = maximumQuantity
        self.currentQuantity = currentQuantity
        self.threshold = threshold


class Solution:
    @staticmethod
    def replenish(inventoryList, limit):
        result = []
        for inv in inventoryList:
            if inv.threshold <= limit:
                result.append(inv)
        return result


if __name__ == "__main__":
    inventory_list = []
    for _ in range(4):
        inventoryId = input()
        maxQ = int(input())
        currQ = int(input())
        threshold = int(input())
        inventory_list.append(Inventory(inventoryId, maxQ, currQ, threshold))

    limit = int(input())
    result_list = Solution.replenish(inventory_list, limit)

    for inv in result_list:
        if inv.threshold >= 75:
            status = "Critical Filling"
        elif 50 <= inv.threshold <= 74:
            status = "Moderate Filling"
        else:
            status = "Non-Critical Filling"
        print(f"{inv.inventoryId} {status}")
