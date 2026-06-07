age=int(input("Enter your age: "))
if (age<=0 or age>120):
    print("Please enter valid age.")
elif (age>=18):
    print(f"{age} are eligible to voting.")
else:
    print(f"{age} are not eligible to voting.")