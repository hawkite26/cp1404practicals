"""
CP1404/CP5632 Practical
Quick Picks

"""
import random
NUMBERS_IN_QUICK_PICK = 6
QUICK_PICK_MINIMUM = 1
QUICK_PICK_MAXIMUM = 45


def main():
    """Gather amount of quick picks and display chosen amount of quick picks."""
    number_of_picks = int(input("How many quick picks? "))
    quick_picks = []
    for i in range(number_of_picks):
        quick_pick = generate_quick_pick(NUMBERS_IN_QUICK_PICK, QUICK_PICK_MINIMUM, QUICK_PICK_MAXIMUM)
        quick_picks.append(quick_pick)
    print_quick_picks(quick_picks)


def generate_quick_pick(number_count, minimum, maximum):
    """Generate quick picks randomly and according to conventions."""
    numbers = []
    while len(numbers) < number_count:
        number = random.randint(minimum, maximum)
        if number not in numbers:
            numbers.append(number)
    numbers.sort()
    return numbers


def print_quick_picks(quick_picks):
    """Display quick picks appropriately."""
    for quick_pick in quick_picks:
        for number in quick_pick:
            print("{:>2}".format(number), end=" ")
        print()


main()
