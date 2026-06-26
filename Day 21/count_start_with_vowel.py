sentence = "Artificial Intelligence is changing our future"
words = sentence.split()

count = 0

for word in words:
    if word[0].lower() in "aeiou":
        count += 1

print("Total Words =", count)