def reverse_words(sentence):
    words = sentence.split()
    reversed_words = [word[::-1] for word in words]
    return " ".join(reversed_words)


if __name__ == "__main__":
    user_input = input("Enter a sentence: ").strip()
    if user_input:
        print(reverse_words(user_input))
    else:
        print("Please enter a sentence.")