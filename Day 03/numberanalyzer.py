num=int(input("Enter a number: "))
count=0
while (num>0):
    num=num//10
    count=count+1
print("Number of digits =", count)

sum = 0

digit = n % 10
sum = sum + digit
n = n // 10

print("Sum of digits =", sum)

reverse = 0

a=n%10
reverse =(reverse*10)+a
n=n//10
print(f"THE REVERSE NUMBER OF THIS NUMBER IS {reverse} .")

original=n
reverse=0

a=n%10
reverse=(reverse*10)+a
n=n//10
if(original==reverse):

    print("The number is  pallindrome number.")
else:print("the number is not  pallindrome number.")