text = input()

reverse = ""

for ch in text:
    reverse = ch + reverse
print(f"The string is : {text}.")
print(f"The reverse string is :{reverse}.")