numbers = [1, 2, 3,4, 5,8,9,7]

n = len(numbers) + 1

expected_sum = n * (n + 1) // 2
actual_sum = sum(numbers)

missing_number = expected_sum - actual_sum

print("Missing Number =", missing_number)