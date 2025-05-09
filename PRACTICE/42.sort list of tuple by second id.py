my_list = [(1, 3), (4, 1), (2, 2), (5, 0)]

# Sort by second item
sorted_list = sorted(my_list, key=lambda x: x[1])

print(sorted_list)
