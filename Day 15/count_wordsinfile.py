file = open("python.txt", "r")

text = file.read()

words = text.split()

print("Total words:", len(words))

file.close()