# Inventory Management System

## Problem Statement

Create a system to manage inventory levels and determine which inventories need replenishing based on their threshold values.

---

### Class: `Inventory`

**Attributes:**
- `inventoryId` (String): ID of the inventory
- `maximumQuantity` (int): Max capacity
- `currentQuantity` (int): Current quantity
- `threshold` (int): Threshold value

**Requirements:**
- Create a parameterized constructor.

---

### Class: `Solution`

**Method:**

#### `replenish(Inventory[], int limit)`
- Takes array of Inventory objects and an integer `limit`.
- Returns list of Inventory objects whose `threshold <= limit`.
- For each returned inventory:
  - If `threshold >= 75` → "Critical Filling"
  - If `50 <= threshold <= 74` → "Moderate Filling"
  - Else → "Non-Critical Filling"

---

### Input:
- 4 Inventory objects with values for: `inventoryId`, `maximumQuantity`, `currentQuantity`, `threshold`
- An integer value `limit`

### Output:
- For each Inventory with threshold ≤ limit:
  - Print `inventoryId` followed by its filling status

---

### Sample Input:
1
100
50
40
2
100
50
50
3
100
40
45
4
100
80
25
45


### Sample Output:
1 Non-Critical Filling
3 Non-Critical Filling
4 Non-Critical Filling
