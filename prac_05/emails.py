"""
CP1404/CP5632 Practical
Email storing system
"""


def main():
    email_to_name = {}
    user_email = input("Email: ")
    while user_email != "":
        possible_name = find_possible_name(user_email)
        user_answer = input("Is your name {}? (Y/n) ".format(possible_name)).lower()
        while user_answer != 'y' and user_answer != 'n' and user_answer != '':
            print("That is an invalid answer")
            user_answer = input("Is your name {}? (Y/n) ".format(possible_name)).lower()
        if user_answer == '' or user_answer == 'y':
            email_to_name[user_email] = possible_name
        elif user_answer == 'n':
            name = input("Name: ").title()
            email_to_name[user_email] = name
        user_email = input("Email: ")
    print(email_to_name)


def find_possible_name(user_email):
    stop_index = user_email.find('@')
    email_name = user_email[:stop_index]
    first_last_name = email_name.split('.')
    if len(first_last_name) == 1:
        possible_name = str(first_last_name[0]).title()
    else:
        possible_name = "{} {}".format(first_last_name[0], first_last_name[-1]).title()
    return possible_name


main()
