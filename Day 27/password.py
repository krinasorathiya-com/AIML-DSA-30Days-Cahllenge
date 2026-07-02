password = input("Enter Password: ")

has_upper = False
has_lower = False
has_digit = False

for ch in password:
    if ch.isupper():
        has_upper = True
    elif ch.islower():
        has_lower = True
    elif ch.isdigit():
        has_digit = True

count = 0

if len(password) >= 8:
    count += 1
if has_upper:
    count += 1
if has_lower:
    count += 1
if has_digit:
    count += 1

if count == 4:
    print("Strong Password")
elif count >= 2:
    print("Medium Password")
else:
    print("Weak Password")