n=int(input("Enter the Number :"))
fact =1
i=1
for i in range(1,n+1):
    fact=(fact*i)
    i+=1

print(f"THE FACTORIAL OF THIS {n} IS {fact}")
