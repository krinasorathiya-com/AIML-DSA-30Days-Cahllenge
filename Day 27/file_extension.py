files = [
    "notes.pdf",
    "resume.pdf",
    "photo.png",
    "music.mp3",
    "movie.mp4",
    "image.png"
]

extensions = {}

for file in files:
    ext = file.split(".")[1]

    if ext in extensions:
        extensions[ext] += 1
    else:
        extensions[ext] = 1

for ext, total in extensions.items():
    print(ext, "->", total)