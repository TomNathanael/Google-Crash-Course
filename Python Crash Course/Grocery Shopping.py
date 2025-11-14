# Sums the prices of items in a shopping basket
def add_prices(basket):
    total = 0  # Start with zero
    for price in basket.values():  # Add each price
        total += price
    return round(total, 2)  # Round to 2 decimal places

groceries = {
    "bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59,
    "coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44
}
print(add_prices(groceries))  # 28.44