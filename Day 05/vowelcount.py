def count_vowels(text):
    count = 0

    for ch in text:
        if ch.lower() in "aeiou":
            count += 1

    print("Number of vowels =", count)

count_vowels("Education")
count_vowels("Hello World")
count_vowels("String")
