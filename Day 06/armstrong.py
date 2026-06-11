num = int(input("Enter a number: "))

temp = num
sum = 0

while (temp > 0):
    digit = temp % 10
    sum = sum + digit**3
    temp = temp // 10

if (sum == num):
    print(f"{num} is the Armstrong .")
else:
    print(f"{num} is  Not Armstrong Number.\n Because cube of digit and their sum is not equal to the {num}.")