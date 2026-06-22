students = {
    "Bhakti": 85,
    "Krina": 72,
    "Meera": 91
}

highest_marks = 0
top_student = ""

for name, marks in students.items():
    if marks > highest_marks:
        highest_marks = marks
        top_student = name

print("Highest Marks Student =", top_student)
print("Marks =", highest_marks)