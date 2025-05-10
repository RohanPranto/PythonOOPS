list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

common = []

for element in list1:
    if element in list2 and element not in common:
        common.append(element)

print("Common elements:", common)
