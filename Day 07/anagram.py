str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
a=str1.islower()
b=str2.islower()
if (sorted(a) == sorted(b)):
    print("Anagram")
else:
    print("Not Anagram")