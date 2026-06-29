grades = {"Aman": "A","Rahul": "B","Priya": "A","Riya": "C","Neha": "B"}

count = {}

for grade in grades.values():
    count[grade] = count.get(grade, 0) + 1

for grade, total in count.items():
    print(grade, "→", total)