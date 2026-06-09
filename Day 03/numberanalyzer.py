num = int(input("Enter a number: "))

original = num

count = 0
temp = num
while temp > 0:
    temp = temp // 10
    count += 1
print("Number of digits =", count)

sum_digits = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum_digits += digit
    temp = temp // 10
print("Sum of digits =", sum_digits)

largest = 0
temp = num
while temp > 0:
    digit = temp % 10
    if digit > largest:
        largest = digit
    temp = temp // 10
print("Largest digit is:", largest)

reverse = 0
temp = num
while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp = temp // 10
print("Reverse number =", reverse)

if original == reverse:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")