n = int(input())
bills = []

for _ in range(n):
    billNo = int(input())
    name = input()
    typeOfConnection = input()
    billAmount = float(input())
    status_input = input()
    if status_input.lower() == "true":
        status = True
    else:
        status = False
    bills.append([billNo, name, typeOfConnection.lower(), billAmount, status])

status_to_check_input = input()
if status_to_check_input.lower() == "true":
    status_to_check = True
else:
    status_to_check = False

type_to_check = input().lower()

# Logic for findBillWithMaxBillAmountBasedOnStatus
max_amount = -1
for i in range(n):
    if bills[i][4] == status_to_check:
        if bills[i][3] > max_amount:
            max_amount = bills[i][3]

matching_bills = []
for i in range(n):
    if bills[i][4] == status_to_check and bills[i][3] == max_amount:
        matching_bills.append([bills[i][0], bills[i][1]])

if len(matching_bills) == 0:
    print("There are no bill with the given status")
else:
    matching_bills.sort()
    for bill in matching_bills:
        print(f"{bill[0]}#{bill[1]}")

# Logic for getCountWithTypeOfConnection
count = 0
for i in range(n):
    if bills[i][2].lower() == type_to_check:
        count += 1

if count == 0:
    print("There are no bills with given type of connection")
else:
    print(count)
