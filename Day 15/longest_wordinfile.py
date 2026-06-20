file = open("python.txt", "r")

text = file.read()

words = text.split()

longest = ""

for word in words:
    if len(word) > len(longest):
        longest = word

file.close()

print("Longest word:", longest)