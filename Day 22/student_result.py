students = {"Aman": 82,"Priya": 95,"Rahul": 61, "Riya": 74}
def average_marks(data):
    return sum(data.values()) / len(data)
def highest_marks(data):
    return max(data.values())
def passed_students(data):
    count = 0
    for marks in data.values():
        if marks >= 35:
            count += 1
    return count
print("Student Result Summary")
print("----------------------")
print("Total Students:", len(students))
print("Average Marks:", average_marks(students))
print("Highest Marks:", highest_marks(students))
print("Passed Students:", passed_students(students))