words = ["artificial","AI", "machine", "learning","python","development"]
words.sort(key=len, reverse=True)
print("Top 3 Longest Words:")
for word in words[:3]:
    print(word)