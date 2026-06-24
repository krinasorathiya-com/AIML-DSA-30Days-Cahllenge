numbers = [1, 2, 3, 4, 5, 6, 7, 8]
groups = {"Even": [], "Odd": []}
for num in numbers:
    if (num % 2 == 0):
        groups["Even"].append(num)
    else:
        groups["Odd"].append(num)
print(groups)