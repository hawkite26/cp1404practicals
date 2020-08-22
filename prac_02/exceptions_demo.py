"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur? When an invalid type is entered, such as a character or string, or a non-integer.
2. When will a ZeroDivisionError occur? Whenever the denominator is selected as zero.
3. Could you change the code to avoid the possibility of a ZeroDivisionError? Yes.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    # The following prevents zero from being the denominator.
    while denominator == 0:
        print("Can't divide by zero.")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
