def average_marks(marks):
    return sum(marks) / len(marks)

def highest_marks(marks):
    return max(marks)

def lowest_marks(marks):
    return min(marks)

def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "D"

student = {
    "name": "Krina",
    "marks": [85, 90, 78, 88]
}

avg = average_marks(student["marks"])

print("Student Name:", student["name"])
print("Average Marks:", avg)
print("Highest Marks:", highest_marks(student["marks"]))
print("Lowest Marks:", lowest_marks(student["marks"]))
print("Grade:", calculate_grade(avg))