"""
CP1404/CP5632 Practical
Word occurrences counter
"""


def main():
    word_to_count = {}
    print("Please enter a sentence or string")
    chosen_string = input(">>> ")
    words = chosen_string.split()
    for word in words:
        if word in word_to_count:
            word_to_count[word] += 1
        else:
            word_to_count[word] = 1
    print(word_to_count)


main()
