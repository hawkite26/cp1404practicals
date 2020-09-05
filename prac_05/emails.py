"""
CP1404/CP5632 Practical
Email storing system
"""


def main():
    user_email = input("Email: ")
    possible_name = find_possible_name(user_email)
    print(possible_name)


def find_possible_name(user_email):
    stop_index = user_email.find('@')
    email_name = user_email[:stop_index]
    first_last_name = email_name.split('.')
    if len(first_last_name) == 1:
        possible_name = str(first_last_name[0])
    else:
        possible_name = "{} {}".format(first_last_name[0], first_last_name[-1]).title()
    return possible_name


main()
