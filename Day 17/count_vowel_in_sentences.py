sentence = "Power Transformer is a preprocessing technique that automatically transforms numerical features to make them closer to a normal distribution.\n It includes Box-Cox and Yeo-Johnson transformations."

count = 0
vowels = "aeiouAEIOU"

for ch in sentence:
    if (ch in vowels):
        count += 1

print("Total Vowels =", count)