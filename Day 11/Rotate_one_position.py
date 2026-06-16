numbers = [5, 4, 3, 2, 1]
last = numbers[-1]

for i in range(len(numbers) - 1, 0, -1):
    numbers[i] = numbers[i - 1]

numbers[0] = last

print(numbers)

