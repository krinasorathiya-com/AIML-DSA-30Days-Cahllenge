text = input("Enter a string: ")

for ch in text:
    count = 0
    for c in text:
        if ch == c:
            count += 1
    print(ch, "=", count)