text = "AI AI ML AI Python ML"

freq = {}
for word in text.split():
    freq[word] = freq.get(word, 0) + 1

most_common = max(freq, key=freq.get)
print(most_common)