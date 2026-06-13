numbers = [1, 2, 3, 2, 4, 5, 1]

visited = set()
duplicates = set()

for num in numbers:
    if num in visited:
        duplicates.add(num)
    else:
        visited.add(num)

print("Duplicate elements:")
for num in duplicates: