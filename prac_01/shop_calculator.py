"""
CP1404/CP5632 - Practical
Shop calculator
"""

DISCOUNT_PRICE = 100
item_count = int(input("Number of items: "))
while item_count <= 0:
    print("Invalid number of items!")
    item_count = int(input("Number of items: "))
total_price = 0
for i in range(item_count):
    item_price = float(input("Price of item: "))
    while item_price <= 0:
        print("Invalid item price!")
        item_price = float(input("Price of item: "))
    total_price += item_price
if total_price > DISCOUNT_PRICE:
    total_price = (total_price/100) * 90
print("Total price for the {} items is ${:.2f}".format(item_count, total_price))
