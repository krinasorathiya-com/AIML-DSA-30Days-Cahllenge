sentence = input("Enter a sentence: ")
words = sentence.split()
total_words = len(words)
total_characters = len(sentence)
longest = words[0]
shortest = words[0]

for word in words:
    if len(word) > len(longest):
        longest = word

    if len(word) < len(shortest):
        shortest = word

print("Total Words:", total_words)
print("Total Characters:", total_characters)
print("Longest Word:", longest)
print("Shortest Word:", shortest)