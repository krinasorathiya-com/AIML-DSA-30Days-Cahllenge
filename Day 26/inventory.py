inventory = {"Laptop": 5, "Keyboard": 0,"Mouse": 8,"Monitor": 2,"Headphones": 0}
available = []
out_of_stock = []
total = 0
for product, qty in inventory.items():
    if (qty > 0):
        available.append(product)
        total += qty
    else:
        out_of_stock.append(product)

print("Available Products:", available)
print("Out of Stock Products:", out_of_stock)
print("Total Available Items:", total)