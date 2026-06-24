marks = {"Aman": [80,90,85], "Priya": [95,88,92], "Rahul": [70,75,80]}
for student, scores in marks.items():
    avg = sum(scores) / len(scores)
    print(f"{student} → {avg:.2f}")