files = ["notes.pdf", "resume.pdf", "photo.jpg", "data.csv", "image.jpg"]
frequency = {}
for file in files:
    extension = file.split(".")[-1]
    frequency[extension] = frequency.get(extension, 0) + 1

for ext, count in frequency.items():
    print(ext, "→", count)