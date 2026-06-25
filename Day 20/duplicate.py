sentence = "AI is amazing AI is powerful"

words = sentence.split()
frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print("Duplicate Words:")
for word, count in frequency.items():
    if count > 1:
        print(word)