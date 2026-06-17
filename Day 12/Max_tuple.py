numbers = (10, 25, 5, 60, 30)

maximum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num

print("Maximum Value =", maximum)