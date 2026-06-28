products = {
    "Laptop": 65000,
    "Mouse": 700,
    "Keyboard": 1500,
    "Monitor": 12000
}

def most_expensive(data):
    name = max(data, key=data.get)
    return name, data[name]

def cheapest(data):
    name = min(data, key=data.get)
    return name, data[name]

def average_price(data):
    return sum(data.values()) / len(data)

exp_name, exp_price = most_expensive(products)
cheap_name, cheap_price = cheapest(products)

print("Most Expensive Product:", exp_name, "-", exp_price)
print("Cheapest Product:", cheap_name, "-", cheap_price)
print("Average Price:", average_price(products))