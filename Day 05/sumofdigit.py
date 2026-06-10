def sumofdigit(a):
    sum=0
    k=a%10
    sum+=k
    a=a//10
print(sum)    
print(f"Sum of digit is {sum}.")   
sumofdigit(1765)
sumofdigit(1234)
sumofdigit(3456)

