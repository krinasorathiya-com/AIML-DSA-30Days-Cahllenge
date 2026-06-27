with open("sample.txt", "r") as file:
    lines = file.readlines()
longest = ""

for line in lines:
    if len(line) > len(longest):
        longest = line

print("Longest Line:")
print(longest.strip())