file = open("sample.txt", "r")

text = file.read()
file.close()

words = text.split()

frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print("Word Frequencies:")

for word, count in frequency.items():
    print(word, "→", count)