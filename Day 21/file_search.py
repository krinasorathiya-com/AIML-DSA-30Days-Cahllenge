word = input("Enter word to search: ")
file = open("python.txt", "r")

content = file.read()
file.close()

if word.lower() in content.lower():
    print("Word Found")
else:
    print("Word Not Found")