sales = {"January": 45000,"February": 52000,"March": 47000,"April": 61000}
def highest_sales(data):
    month = max(data, key=data.get)
    return month, data[month]
def lowest_sales(data):
    month = min(data, key=data.get)
    return month, data[month]
def average_sales(data):
    return sum(data.values()) / len(data)

high_month, high_value = highest_sales(sales)
low_month, low_value = lowest_sales(sales)
print("Highest Sales Month:", high_month, "-", high_value)
print("Lowest Sales Month:", low_month, "-", low_value)
print("Average Sales:", average_sales(sales))