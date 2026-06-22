sentence = "Machine Learning Is Amazing"

count = 0
vowels = "aeiouAEIOU"

for ch in sentence:
    if ch in vowels:
        count += 1

print("Total Vowels =", count)