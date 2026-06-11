nums = list(map(int, input().split()))

largest = 0
second = 0

for num in nums:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

print(second)