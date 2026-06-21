file = open("p.txt", "r")

text = file.read()

file.close()

lines = text.split("\n")
words = text.split()

print("Lines      :", len(lines))
print("Words      :", len(words))
print("Characters :", len(text))