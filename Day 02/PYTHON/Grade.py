mark = int(input("Enter Marks: "))
if (mark <= 0 or mark > 100):
    print("Please enter valid marks!")
elif (mark < 60):
    print("Grade: F")
    print("You are fail in this exam.")
elif (mark < 70):
    print("Grade: D")
elif (mark < 80):
    print("Grade: C")
elif (mark < 90):
    print("Grade: B")
else:
    print("Grade: A")
    print("EXCELLENT PERFORMANCE!")
