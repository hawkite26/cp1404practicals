"""CP1404/CP5632 Practical - Programming guitar program"""

from prac_06.guitar import Guitar


def main():
    print("My guitars!")
    my_guitars = []
    guitar_name = input("Guitar name: ")
    while guitar_name != "":
        guitar_year = int(input("Year: "))
        guitar_cost = float(input("Cost: $"))
        guitar = Guitar(guitar_name, guitar_year, guitar_cost)
        my_guitars.append(guitar)
        my_guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
        my_guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
        guitar_name = input("Guitar name: ")
    for i, guitar in enumerate(my_guitars, 1):
        if guitar.is_vintage() is True:
            print("Guitar {}: {:<20} ({}), worth ${:<10,.2f} (vintage)".format(i, guitar.name, guitar.year, guitar.cost))
        else:
            print("Guitar {}: {:<20} ({}), worth ${:<10,.2f}".format(i, guitar.name, guitar.year, guitar.cost))


main()
