def file_analysis(filename):
    file = open(filename, "r")

    text = file.read()
    file.close()

    words = text.split()

    longest = ""

    for word in words:
        if (len(word) > len(longest)):
            longest = word

    print("Longest Word:", longest)
    print("Total Characters:", len(text))

file_analysis("sample.txt")