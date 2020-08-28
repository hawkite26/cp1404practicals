"""
CP1404/CP5632 Practical
Numbers list program
"""

USERNAMES = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']


def main():
    check_valid_username(USERNAMES)
    numbers = []
    for i in range(5):
        number = check_valid_number()
        numbers.append(number)
    print_number_info("first", numbers[0])
    print_number_info("last", numbers[-1])
    print_number_info("smallest", min(numbers))
    print_number_info("largest", max(numbers))
    print("The average of the numbers is {}".format(sum(numbers)/len(numbers)))


def check_valid_username(usernames):
    valid_username = False
    while not valid_username:
        username = input("Please enter username: ")
        if username in usernames:
            print("Access Granted")
            valid_username = True
        else:
            print("Access Denied")


def check_valid_number():
    valid_entry = False
    while not valid_entry:
        try:
            number = int(input("Please enter a number: "))
            valid_entry = True
        except ValueError:
            print("That is an invalid entry.")
    return number


def print_number_info(definition, number):
    print("The {} number is {}".format(definition, number))


main()
