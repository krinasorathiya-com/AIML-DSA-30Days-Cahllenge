def sumofdigit(a):
    total = 0

    while (a > 0):
        digit = a % 10
        total += digit
        a = a // 10

    print(f"Sum of digits is {total}")

sumofdigit(1765)
sumofdigit(1234)
sumofdigit(3456)