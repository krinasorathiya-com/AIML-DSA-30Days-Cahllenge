text = "Python is great and Python is easy"
freq = {}
for word in text.lower().split():
    freq[word] = freq.get(word, 0) + 1
for word, count in freq.items():
    print(f"{word} → {count}")