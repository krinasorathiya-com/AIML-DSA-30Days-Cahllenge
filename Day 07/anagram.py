str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if (sorted(str1.islower()) == sorted(str2.islower())):
    print("Anagram")
else:
    print("Not Anagram")