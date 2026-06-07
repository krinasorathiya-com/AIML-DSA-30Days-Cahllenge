name=input("Enter your name: ")
age=int(input("Enter your age: "))
Marks=int(input("Enter your marks: "))
if (Marks <= 0 or Marks > 100):
    print("Please enter valid marks!")
elif (Marks < 60):
    print("Grade: F")
    print("Status:Fail") 
elif (Marks < 70):
    print("Grade: D") 
    print("Status:Pass")   
elif (Marks < 80):
    print("Grade: C")
    print("Status:Pass")        
elif (Marks < 90):
    print("Grade: B")
    print("Status:Pass") 
else:
    print("Grade: A")
    print("Status:Pass") 
    print("EXCELLENT PERFORMANCE!") 