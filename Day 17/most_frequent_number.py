numbers = [78,98,78,87,78,56,34,43,12,21,89,78,78]
frequency = {}
for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

max_count = 0
answer = 0

for key, value in frequency.items():
    if (value > max_count):
        max_count = value
        answer = key

print("Most Frequent Number =", answer)