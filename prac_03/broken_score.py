"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    score = float(input("Enter score: "))
    if score < 0 or score > 100:
        print("Invalid score")
    else:
        result = determine_result(score)
        print("Your score of {} is {}".format(score, result))


def determine_result(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    elif score < 50:
        return "Bad"


def generate_random_score():
    random_score = random.randint(0, 101)
    result = determine_result(random_score)
    print("The random score of {} is {}".format(random_score, result))


main()
