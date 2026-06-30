students = {
    "Aman": [85, 92, 88],
    "Priya": [95, 96, 91],
    "Rahul": [70, 72, 75]
}

def average_marks(data):
    averages = {}

    for student, marks in data.items():
        avg = sum(marks) / len(marks)
        averages[student] = avg
        print(student, "Average:", avg)

    highest = max(averages, key=averages.get)
    lowest = min(averages, key=averages.get)

    print("Highest Average:", highest, "->", averages[highest])
    print("Lowest Average:", lowest, "->", averages[lowest])

average_marks(students)