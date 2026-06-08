num=int(input("Enter a number: "))
count=0
while (num>0):
    num=num//10
    count=count+1
print("Number of digits =", count)

sum = 0

digit = num% 10
sum = sum + digit
num = num // 10

print("Sum of digits =", sum)

reverse = 0

a=num%10
reverse =(reverse*10)+a
num=num//10
print(f"THE REVERSE NUMBER OF THIS NUMBER IS {reverse} .")

original=num
reverse=0

a=num%10
reverse=(reverse*10)+a
num=num//10
if(original==reverse):

    print("The number is  pallindrome number.")
else:print("the number is not  pallindrome number.")