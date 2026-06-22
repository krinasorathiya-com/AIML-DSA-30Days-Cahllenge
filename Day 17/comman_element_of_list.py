list1 = [11,67,23,45,890,80,78]
list2 = [12,67,89,34,80]

common = set(list1) & set(list2)

print("Common Elements:")

for num in common:
    print(num)