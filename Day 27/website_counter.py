visitors = [
    "India",
    "USA",
    "India",
    "Canada",
    "USA",
    "India",
    "Germany"
]

count = {}

for country in visitors:
    if (country in count):
        count[country] += 1
    else:
        count[country] = 1

for country, total in count.items():
    print(country, "->", total)