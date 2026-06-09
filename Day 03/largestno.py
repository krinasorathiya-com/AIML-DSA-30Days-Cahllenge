num = int(input("Enter the number: "))
large =0
while (num > 0):
    a = num % 10
    if(large<a):
        print(f"Largest digit is: {a}.")
    else:
        print(f"Largest number is : {large}")    
num = num // 10


