employees = [ ("Aman", "HR"), ("Rahul", "IT"), ("Priya", "IT"), ("Neha", "HR"), ("Riya", "Finance")]

def department_counter(data):
    count = {}
    for name, dept in data:
        if (dept in count):
            count[dept] += 1
        else:
            count[dept] = 1

    for dept, total in count.items():
        print(dept, "->", total)

department_counter(employees)