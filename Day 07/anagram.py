str1 = input("Enter first string: ").lower()
str2 = input("Enter second string: ").lower()

if sorted(str1) == sorted(str2):
    print(f"{str1} and {str2} is Anagram.")
else:
    print(f"{str1} and {str2} is Not Anagram.")