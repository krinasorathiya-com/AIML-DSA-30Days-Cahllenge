n=int(input("Enter the number : "))
original=n
reverse=0
while(n>0):
    a=n%10
    reverse=(reverse*10)+a
    n=n//10
print(f"The reverse number is: {reverse}")
if(original==reverse):

    print("The number is  pallindrome number.")
else:print("the number is not  pallindrome number.")