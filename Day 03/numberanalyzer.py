num=int(input("Enter a number: "))
count=0
sum=0
largest=0
reverse =0

while (num>0):
    num=num//10
    count=count+1
print("Number of digits =", count)

digit = num% 10
sum = sum + digit
num = num // 10

print("Sum of digits =", sum)

while (num > 0):
    digit = num % 10

    if (digit > largest):
        largest = digit

    num = num // 10

print("Largest digit is:", largest)

a=num%10
reverse =(reverse*10)+a
num=num//10
print(f"THE REVERSE NUMBER OF THIS NUMBER IS {reverse} .")

original=num
a=num%10
reverse=(reverse*10)+a
num=num//10
if(original==reverse):

    print("The number is  pallindrome number.")
else:print("the number is not  pallindrome number.")