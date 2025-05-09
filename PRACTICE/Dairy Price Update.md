# Dairy Product and Grade Price Adjustment System

## Problem Statement

You are required to create two classes to manage a list of dairy products and update their prices based on a weightage system tied to their grades.

---

### Class 1: `DairyProduct`

**Attributes:**
- `id`: Number
- `brand`: String
- `type`: String
- `price`: Number
- `grade`: String

**Methods:**
- `__init__`: Takes all 5 values in the above order and initializes all attributes.
- `-JLiL-` (you can name it meaningfully in code): Takes all 5 parameters in same order and only updates the `price` and `grade`.

---

### Class 2: `ProductGrade`

**Attributes:**
- `dairyList`: A list of `DairyProduct` objects
- `weightageDict`: A dictionary with grade as key and weightage (int) as value.

**Methods:**
- `__init__`: Initializes the list and dictionary as above.
- `priceBasedOnBrandAndType(brand, type)`: 
  - Case-insensitive comparison.
  - Filters products from `dairyList` matching both brand and type.
  - Calculates updated price using the formula:  
    `updated_price = price + (price * weightage / 100)`
  - Updates the price of matching products.
  - Returns the list of matching updated `DairyProduct` objects.
  - If no match found, return `None`.

---

## Input Format (for main program)
1. Read number of dairy products.
2. For each dairy product, read:
    - `id`, `brand`, `type`, `price`, `grade`
3. Read number of dictionary entries.
4. For each entry, read `grade` and `weightage`.
5. Read a brand and type to filter.
6. Call `priceBasedOnBrandAndType()` and print results.

---

## Output Format
- If product found and updated, print:  
  `<brand> <updated_price>`
- Else print:  
  `No dairy product found`

---

## Sample Input
