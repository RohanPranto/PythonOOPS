# Electricity Billing System

## Class: Bill

**Attributes (all private):**
- `billNo`: int  
- `name`: String  
- `typeOfConnection`: String (prepaid or postpaid)  
- `billAmount`: float  
- `status`: boolean (True = paid, False = not paid)

### Methods:
- Parameterized constructor for all attributes.
- Getters and setters for all attributes.

---

## Class: Solution

### Static Methods:

#### `findBillWithMaxBillAmountBasedOnStatus(bill_list, status)`
- Takes list of `Bill` objects and a boolean `status`.
- Finds all bills with the given `status`.
- Among them, finds the bill(s) with maximum `billAmount`.
- Returns list of those bills sorted by `billNo` (ascending).
- Returns `None` if no bill with that status is found.

#### `getCountWithTypeOfConnection(bill_list, connection_type)`
- Takes list of `Bill` objects and a string connection type.
- Returns count of bills where `typeOfConnection` matches.
- Case-insensitive check.
- Returns 0 if no matching bill found.

---

## Input Format
- First, read number of bills `n`
- For each bill, read:  
  `billNo`, `name`, `typeOfConnection`, `billAmount`, `status`
- Read a boolean (for status search)
- Read a string (for type of connection search)

---

## Output Format

- **findBillWithMaxBillAmountBasedOnStatus**:
  - If result found, print each as `billNo#name`
  - Else print `There are no bill with the given status`

- **getCountWithTypeOfConnection**:
  - If result > 0, print the number
  - Else print `There are no bills with given type of connection`

---

### Sample Input
4
111
Aman Mittal
Prepaid
914.25
true
222
Rekha Kumar
Prepaid
1425.75
false
333
Samyra Gupta
Prepaid
1305.00
true
444
Mohit Saxena
Postpaid
1300.50
false
false
Prepaid


### Sample Output
222#Rekha Kumar
3