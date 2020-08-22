"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = float(input("Enter sales: $"))
while sales >= 0:
    one_percent_sales = (sales/100)
    if sales < 1000:
        user_bonus = one_percent_sales * 10
    else:
        user_bonus = one_percent_sales * 15
    print("Sales: ${:.2f}\nBonus: ${:.2f}".format(sales, user_bonus))
    sales = float(input("Enter sales: $"))
