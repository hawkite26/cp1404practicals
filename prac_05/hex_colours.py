"""
CP1404/CP5632 Practical
State colours hex codes in a dictionary
"""

COLOUR_TO_HEX = {"white": "#ffffff", "black": "#000000", "blue1": "#0000ff", "red1": "#ff0000", "green1": "#00ff00",
                 "hotpink": "#ff69b4", "magenta": "#ff00ff", "turquoise": "#40e0d0", "yellow1": "#ffff00",
                 "lightskyblue": "#87cefa"}


def main():
    display_valid_colours()
    chosen_colour = input("Please enter a colour name: ").lower()
    while chosen_colour != "":
        if chosen_colour in COLOUR_TO_HEX:
            print("{} is {}". format(chosen_colour, COLOUR_TO_HEX[chosen_colour]))
        else:
            print("Invalid colour")
        chosen_colour = input("Please enter a colour name: ").lower()


def display_valid_colours():
    for colour in COLOUR_TO_HEX:
        print(colour, end=", ")
    print()


main()
