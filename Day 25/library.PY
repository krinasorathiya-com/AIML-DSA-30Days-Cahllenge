books = {"Python": 5,"AI": 2,"DSA": 4,"ML": 1}

def available_books(data):
    print("Available Books:")
    for book, qty in data.items():
        if (qty > 0):
            print(book)
def unavailable_books(data):
    print("Unavailable Books:")
    found = False
    for book, qty in data.items():
        if (qty == 0):
            print(book)
            found = True
    if not found:
        print("None")
def total_books(data):
    print("Total Books:", sum(data.values()))

available_books(books)
unavailable_books(books)
total_books(books)