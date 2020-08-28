"""
CP1404/CP5632 Practical
Quick Picks

"""
import random
NUMBERS_IN_QUICK_PICK = 6
QUICK_PICK_MINIMUM = 1
QUICK_PICK_MAXIMUM = 45


def main():
    number_of_picks = int(input("How many quick picks would you like to generate? "))
    quick_picks = []
    for i in range(number_of_picks):
        quick_pick = generate_quick_pick(NUMBERS_IN_QUICK_PICK, QUICK_PICK_MINIMUM, QUICK_PICK_MAXIMUM)
        quick_picks.append(quick_pick)
    print(quick_picks)


def generate_quick_pick(number_count, minimum, maximum):
    numbers = []
    while len(numbers) < number_count:
        number = random.randint(minimum, maximum)
        if number not in numbers:
            numbers.append(number)
    return numbers


main()
