str1 = "Good"
str2 = "Afternoon"

common = set(str1) & set(str2)

for ch in common:
    print(ch, end=" ")