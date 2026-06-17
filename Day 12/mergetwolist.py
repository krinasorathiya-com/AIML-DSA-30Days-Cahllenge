list1 = [1, 2, 3]
list2 = [3, 4, 5]

result = []

for item in list1:
    if (item not in result):
        result.append(item)

for item in list2:
    if item not in result:
        result.append(item)

print(result)