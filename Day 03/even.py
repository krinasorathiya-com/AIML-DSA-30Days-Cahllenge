print(" EVEN number list : ")
num1 =int(input("Enter the first  number : "))
num2 = int(input("Enter the second number : "))
for i in range((num1), (num2) + 1):
    if(i<=0): print("Please enter a positive number")
        
    elif(i % 2 == 0): print(f"{i}")
    print("All the even numbers between", num1, "and", num2, "are printed above.")
    else:print("Please Enter number not string.")

