def word_frequency(sentence):
    freq = {}
    for word in sentence.split():
        freq[word] = freq.get(word, 0) + 1
    for word, count in freq.items():
        print(f"{word} → {count}")

word_frequency("Python is fun, Python is powerful.")