marks = {"Aman": [80,90,85], "Priya": [95,88,92], "Rahul": [70,75,80]}
best_student = None
best_avg = 0
for student, scores in marks.items():
    avg = sum(scores) / len(scores)
    if avg > best_avg:
        best_avg = avg
        best_student = student

print(f"{best_student} → {best_avg:.2f}")