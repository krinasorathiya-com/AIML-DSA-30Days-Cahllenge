text = input("Enter a string: ")

for ch in text:
    if (text.count(ch) == 1):
        print(f"{ch} is First non repeating character.")
        break