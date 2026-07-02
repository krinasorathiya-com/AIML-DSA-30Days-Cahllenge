def calculate_average(scores):
    return sum(scores) / len(scores)
employees = {
    "Aman": [85, 90, 88],
    "Priya": [92, 95, 94],"Rahul": [70, 75, 72],"Neha": [98, 96, 99]}
averages = {}
for name, scores in employees.items():
    avg = calculate_average(scores)
    averages[name] = avg
    print(name, "Average Score:", round(avg, 2))
best = max(averages, key=averages.get)
lowest = min(averages, key=averages.get)
print("\nBest Performer:", best)
print("Lowest Performer:", lowest)