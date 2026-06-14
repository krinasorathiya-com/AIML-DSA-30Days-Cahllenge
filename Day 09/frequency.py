text = "banana"

frequency = {}

for ch in text:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

for key, value in frequency.items():
    print(f"{key} = {value}")