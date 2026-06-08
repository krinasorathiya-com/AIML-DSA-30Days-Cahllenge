n=int(input("Enter the number : "))
reverse = 0
while(n>0):
    a=n%10
    reverse =(reverse*10)+a
    n=n//10
print(f"THE REVERSE NUMBER OF THIS NUMBER IS {reverse} .")    