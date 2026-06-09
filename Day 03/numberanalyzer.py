num = int(input("Enter a number: "))

original = num

count = 0
temp = num
while (temp > 0):
    temp = temp // 10
    count += 1
print("Number of digits =", count)

sum_digits = 0
temp1 = num
while (temp > 0):
    digit = temp1 % 10
    sum_digits += digit
    temp1 = temp1 // 10
print("Sum of digits =", sum_digits)

largest = 0
temp2 = num
while (temp > 0):
    digit = temp2 % 10
    if digit > largest:
        largest = digit
    temp2 = temp2 // 10
print("Largest digit is:", largest)

reverse = 0
temp3 = num
while (temp > 0):
    digit = temp3 % 10
    reverse = reverse * 10 + digit
    temp3 = temp3 // 10
print("Reverse number =", reverse)

if original == reverse:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")