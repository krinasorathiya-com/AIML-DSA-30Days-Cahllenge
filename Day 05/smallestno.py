def small(a,b,c):
    a=int(input("Enter the first number : "))
    b=int(input("Enter the second number : "))
    c=int(input("Enter the third number :"))
    if(a<c or a<b):
        print(f"{a} is smallest number in this all number.")
    elif(b<c or b<a):
        print(f"{b} is the smallest number in this all number.")
    else:
        print(f"{c} is smallest number in this all number.")
small(23,567,-99)
small(-45,0,56785)
small(9,45,88)



    