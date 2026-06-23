def most_frequent(words):
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    max_word = None
    max_count = 0
    for word, count in freq.items():
        if (count > max_count):
            max_count = count
            max_word = word
    return max_word

print(most_frequent(["AI","ML","AI","Python","AI","ML"]))