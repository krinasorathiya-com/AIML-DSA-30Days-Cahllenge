numbers = [21,45,88,90,87,12,-45]

smallest = float('inf')
second_smallest = float('inf')

for num in numbers:
    if num < smallest:
        second_smallest = smallest
        smallest = num
    elif num < second_smallest and num != smallest:
        second_smallest = num

print("Second Smallest =", second_smallest)