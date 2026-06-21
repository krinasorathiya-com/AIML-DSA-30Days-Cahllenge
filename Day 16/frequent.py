numbers = [1, 2, 2, 3, 1, 2, 4]
frequency = {}

for num in numbers:
    if (num in frequency):
        frequency[num] += 1
    else:
        frequency[num] = 1

most_frequent = None
max_count = 0

for key, value in frequency.items():
    if value > max_count:
        max_count = value
        most_frequent = key

print("Most Frequent Element:", most_frequent)