text = input("Enter a string: ")
ch = input("Enter character to count: ")

count = 0

for c in text:
    if c == ch:
        count += 1

print(f"{ch} is in {text} is {count} times.")