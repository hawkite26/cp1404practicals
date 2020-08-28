"""
CP1404/CP5632 Practical
Numbers list program
"""


def main():
    numbers = []
    for i in range(5):
        valid_entry = False
        while not valid_entry:
            try:
                number = int(input("Please enter a number: "))
                numbers.append(number)
                valid_entry = True
            except ValueError:
                print("That is an invalid entry.")
    return numbers


main()
