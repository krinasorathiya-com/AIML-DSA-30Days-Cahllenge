numbers = [1, 2, 3, 9, 8, 5, 1]

print("Duplicate Elements:")

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if (numbers[i] == numbers[j]):
            print(numbers[i])
            break