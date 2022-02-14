import random


def get_random_word():
    # open words.txt
    file = open("words.txt", "r")
    line = next(file)

    # find random word of any length
    for num, aline in enumerate(file, 2):
        if random.randrange(num):
            continue

        line = aline.strip()

    return line


def get_random_5_letter_word():
    word = get_random_word()

    # check if word is of length 5
    while len(word) != 5:
        word = get_random_word()
    else:
        return word
