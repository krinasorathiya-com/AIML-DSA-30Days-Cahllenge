numbers = [2, 5, 7, 2, 4, 5, 8, 2]
frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print("Duplicate Numbers:")

for key, value in frequency.items():
    if value > 1:
        print(key)