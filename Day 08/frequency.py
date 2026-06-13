text = input("Enter a string: ")

visited = ""

for ch in text:
    if ch not in visited:
        count = 0
        for c in text:
            if ch == c:
                count += 1
        print(ch, "=", count)
        visited += ch