"""CP1404 Kye Bryce Prac 3 Password Checker"""


def main():
    minimum_length = 7
    password = get_password(minimum_length)
    print_asterisks(password)


def print_asterisks(password):
    print("Your password is ", len(password) * "*", " long.", sep="")


def get_password(minimum_length):
    password = input("Please enter a username with at least {} characters: ".format(minimum_length))
    while len(password) < minimum_length:
        print("Invalid length.")
        password = input("Please enter a username with at least {} characters: ".format(minimum_length))
    return password


main()
