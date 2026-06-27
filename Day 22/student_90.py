attendance = {
    "Aman": 92,
    "Priya": 85,
    "Rahul": 74,
    "Riya": 98
}
print("Students with attendance above 90%:")

for student, percent in attendance.items():
    if percent > 90:
        print(student)