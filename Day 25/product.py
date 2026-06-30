products = [
    ("Laptop", "Electronics"),
    ("Phone", "Electronics"),
    ("Chair", "Furniture"),
    ("Table", "Furniture"),
    ("Bottle", "Kitchen")
]

def category_count(data):
    categories = {}

    for product, category in data:
        if category in categories:
            categories[category] += 1
        else:
            categories[category] = 1

    for category, count in categories.items():
        print(category, "->", count)

category_count(products)