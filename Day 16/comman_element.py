list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

common = list(set(list1) & set(list2))
print("There is all common elements.")
print(common)