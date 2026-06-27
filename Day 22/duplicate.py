sentence = "AI AI Machine Learning Learning AI"
words = sentence.split()

seen = set()

print("Words without duplicates:")

for word in words:
    if word not in seen:
        print(word)
        seen.add(word)