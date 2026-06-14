text = "banana"

frequency = {}

# Count frequency of each character
for ch in text:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

# Print the frequency
for key, value in frequency.items():
    print(f"{key} = {value}")