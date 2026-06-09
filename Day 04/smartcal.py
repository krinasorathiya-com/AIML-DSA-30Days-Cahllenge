def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Division by zero is not possible!"
    return a / b

def largest(a, b):
    if a > b:
        return a
    else:
        return b

def odd_even(n):
    if n % 2 == 0:
        return "Even Number"
    else:
        return "Odd Number"


print("===== SMART CALCULATOR =====")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Largest Number")
print("6. Odd/Even Check")

choice = int(input("Enter your choice (1-6): "))

if (choice == 1):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("Result =", addition(num1, num2))

elif (choice == 2):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("Result =", subtraction(num1, num2))

elif (choice == 3):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("Result =", multiplication(num1, num2))

elif (choice == 4):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("Result =", division(num1, num2))

elif (choice == 5):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("Largest Number =", largest(num1, num2))

elif (choice == 6):
    num = int(input("Enter a number: "))
    print(odd_even(num))

else:
    print("Invalid Choice!")