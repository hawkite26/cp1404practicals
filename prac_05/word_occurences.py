"""
CP1404/CP5632 Practical
Word occurrences counter
"""


from operator import itemgetter
FIRST_LETTER = 0


def main():
    chosen_string = input("Text: ").lower()
    words = chosen_string.split()
    words.sort()
    word_to_count = count_words(words)
    for word in word_to_count:
        print("{} : {}".format(word, word_to_count[word]))


def count_words(words):
    word_to_count = {}
    for word in words:
        if word in word_to_count:
            word_to_count[word] += 1
        else:
            word_to_count[word] = 1
    return word_to_count


main()
