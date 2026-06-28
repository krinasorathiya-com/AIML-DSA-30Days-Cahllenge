students = {"Aman": 82, "Priya": 45,"Rahul": 76,"Riya": 39,"Neha": 91}
passing_marks = 50
passed = 0
failed = 0

for marks in students.values():
    if (marks >= passing_marks):
        passed += 1
    else:
        failed += 1

total = len(students)
pass_percentage = (passed / total) * 100
fail_percentage = (failed / total) * 100
print("Pass Percentage:", pass_percentage, "%")
print("Fail Percentage:", fail_percentage, "%")