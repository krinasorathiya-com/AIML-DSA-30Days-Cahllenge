def highest_salary(employee):
    name = max(employee, key=employee.get)
    return name, employee[name]
def lowest_salary(employee):
    name = min(employee, key=employee.get)
    return name, employee[name]
def average_salary(employee):
    return sum(employee.values()) / len(employee)

employees = {
    "Aman": 35000,
    "Priya": 52000,
    "Rahul": 47000,
    "Riya": 61000
}

high_name, high_salary = highest_salary(employees)
low_name, low_salary = lowest_salary(employees)
avg = average_salary(employees)

print("Highest Salary:", high_name, "-", high_salary)
print("Lowest Salary:", low_name, "-", low_salary)
print("Average Salary:", avg)