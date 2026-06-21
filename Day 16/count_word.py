sentence = "machine learning is not harder than programming language."

words = sentence.split()

frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

for key, value in frequency.items():
    print(key, "→", value)