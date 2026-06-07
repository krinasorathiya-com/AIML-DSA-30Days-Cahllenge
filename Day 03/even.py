print(" EVEN number list : ")
num1 =float(input("Enter the first  number : "))
num2 = float(input("Enter the second number : "))
for i in range((num1), (num2) + 1):
    if(i<=0): print("Please enter a positive number")
        
    elif(i % 2 == 0): print(f''' {i}  \n All number are EVEN.''')
    else:print("Please Enter number not string.")

