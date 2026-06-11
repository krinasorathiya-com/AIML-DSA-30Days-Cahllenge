def countvowel(a):
    a = input("Enter a string: ")

count = 0

for ch in a.lower():
    if ch in "aeiou":
        count += 1

print(count)
countvowel(Education)
countvowel(Banana)

    