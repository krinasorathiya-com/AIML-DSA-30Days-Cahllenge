num = int(input("Enter the number: "))
large = 0

while (num > 0):
    a = num % 10

if (a > large):
        large = a
        num = num // 10

print(f"The largest digit in this number is {large}")