numbers = (12,34,56,78,12,34,90,12)
target = 12

count = 0

for num in numbers:
    if (num == target):
        count += 1

print("Occurrence =", count)