numbers = [1, 2, 2, 3, 4, 4, 5]
frequency = {}

for num in numbers:
    if (num in frequency):
        frequency[num] += 1
    else:
        frequency[num] = 1

print("Unique Elements:")

for key, value in frequency.items():
    if value == 1:
        print(key, end=" ")