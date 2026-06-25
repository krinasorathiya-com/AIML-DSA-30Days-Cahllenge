from pathlib import Path

file_path = Path(__file__).with_name("python.txt")

with file_path.open("r", encoding="utf-8") as file:
    text = file.read()

words = text.split()
frequency = {}
for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print("Word Frequencies:")
for word, count in sorted(frequency.items()):
    print(f"{word} → {count}")