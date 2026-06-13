text = input("Enter a string: ")

if (text.lower() == text.lower()[::-1]):
    print(" String is Palindrome.")
else:
    print("String is Not Palindrome.")