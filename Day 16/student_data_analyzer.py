def find_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "Fail"

name = input("Enter student name: ")
marks = int(input("Enter marks: "))

grade = find_grade(marks)

print("Name :", name)
print("Marks:", marks)
print("Grade:", grade)