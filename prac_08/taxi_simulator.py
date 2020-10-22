"""
CP1404
Taxi Simulation Program
"""

from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer",
                                                                                      200, 4)]
    current_taxi = None
    total_fare = 0
    display_menu()
    user_choice = get_user_choice()
    while user_choice != "q":
        if user_choice == "c":
            display_taxis(taxis)
            taxi_choice = get_taxi_choice(taxis)
            current_taxi = taxis[taxi_choice]
            display_total_fare(total_fare)
        if user_choice == "d":
            current_taxi.drive(int(input("Drive how far? ")))
            current_fare = current_taxi.get_fare()
            taxi_name = get_taxi_name(current_taxi)
            print("Your {} fare cost you {:.2f}".format(taxi_name, current_fare))
            total_fare = calculate_total_fare(total_fare, current_fare)
            current_taxi.start_fare()
            display_total_fare(total_fare)
        display_menu()
        user_choice = get_user_choice()
    print("Total trip cost: ${:.2f}".format(total_fare))
    print("Taxis are now:")
    display_taxis(taxis)


def get_taxi_name(current_taxi):
    taxi_name = current_taxi
    taxi_name = str(taxi_name).split()
    taxi_name = taxi_name[0].split(",")
    taxi_name = taxi_name[0]
    return taxi_name


def display_menu():
    """Display choice menu"""
    print("Let's drive!")
    print("q)uit, c)hoose taxi, d)rive")


def get_user_choice():
    """Get valid user choice"""
    user_choice = input(">>> ")
    while user_choice not in ["q", "c", "d"]:
        print("Invalid choice")
        user_choice = input(">>> ")
    return user_choice


def display_taxis(taxis):
    current_taxi_index = 0
    for taxi in taxis:
        print("{} - {}".format(current_taxi_index, taxi))
        current_taxi_index += 1


def get_taxi_choice(taxis):
    taxi_choice = int(input("Choose taxi: "))
    while taxi_choice < 0 or taxi_choice > (len(taxis) - 1):
        print("Invalid choice")
        taxi_choice = int(input("Choose taxi: "))
    return taxi_choice


def calculate_total_fare(total_fare, current_fare):
    total_fare += current_fare
    return total_fare


def display_total_fare(total_fare):
    print("Bill to date: ${:.2f}".format(total_fare))


main()