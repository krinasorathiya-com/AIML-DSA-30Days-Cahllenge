word = "Python"

with open("sample.txt", "r") as file:
    text = file.read()

words = text.split()

count = 0
for w in words:
    if (w == word):
        count += 1

print("Total Occurrences:", count)