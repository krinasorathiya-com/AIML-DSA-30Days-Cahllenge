def file_statistics(filename):
    file = open(filename, "r")

    text = file.read()
    file.close()

    lines = text.split("\n")
    words = text.split()

    longest = ""

    for word in words:
        if (len(word) > len(longest)):
            longest = word

    print("Total Lines:", len(lines))
    print("Total Words:", len(words))
    print("Total Characters:", len(text))
    print("Longest Word:", longest)

file_statistics("python.txt")
