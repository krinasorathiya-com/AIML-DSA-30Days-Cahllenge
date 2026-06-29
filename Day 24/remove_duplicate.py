students = ["Aman", "Priya", "Aman", "Rahul", "Priya", "Riya"]

unique = []
seen = set()

for name in students:
    if (name not in seen):
        unique.append(name)
        seen.add(name)

print("Unique Student Names:", unique)