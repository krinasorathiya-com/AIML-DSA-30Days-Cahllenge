list1 = [11, 56,90,11]
list2 = [45,89,66,90]

result = []

for item in list1:
    if (item not in result):
        result.append(item)

for item in list2:
    if (item not in result):
        result.append(item)

print(result)