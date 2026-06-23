def group_by_grade(students):
    groups = {}
    for name, grade in students:
        if (grade not in groups):
            groups[grade] = []
        groups[grade].append(name)
    for grade, names in groups.items():
        print(f"{grade} → {', '.join(names)}")
data = [("Meera","A"),("Krina","B"),("Bhakti","A"),("Riya","C")]
group_by_grade(data)