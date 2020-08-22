"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH = 5
MAX_LENGTH = 15
SPECIAL_CHARS_REQUIRED = True
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH,
          "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print("Your {}-character password is valid: {}".format(len(password),
                                                           password))


def is_valid_password(password):
    """Determine if the provided password is valid."""
    print(len(password))
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        return False
    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    for char in password:
        if char.islower():
            count_lower += 1
        if char.isupper():
            count_upper += 1
        if char.isdigit():
            count_digit += 1
        if SPECIAL_CHARS_REQUIRED is True:
            for character in SPECIAL_CHARACTERS:
                if char == character:
                    count_special += 1
    if count_lower == 0:
        return False
    if count_upper == 0:
        return False
    if count_digit == 0:
        return False
    if SPECIAL_CHARS_REQUIRED is True:
        if count_special == 0:
            return False
    return True


main()
