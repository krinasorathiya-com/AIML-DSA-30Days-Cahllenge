attendance = {
    "Aman": 92,
    "Priya": 81,
    "Rahul": 65,
    "Neha": 98,
    "Riya": 74
}

def average_attendance(data):
    return sum(data.values()) / len(data)

def highest_attendance(data):
    student = max(data, key=data.get)
    print("Highest Attendance:", student, "->", data[student])

def lowest_attendance(data):
    student = min(data, key=data.get)
    print("Lowest Attendance:", student, "->", data[student])

def above_average(data, avg):
    print("Students Above Average:")
    for student, att in data.items():
        if att > avg:
            print(student, "->", att)

avg = average_attendance(attendance)
highest_attendance(attendance)
lowest_attendance(attendance)
print("Average Attendance:", avg)
above_average(attendance, avg)