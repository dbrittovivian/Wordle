import random
import unittest


def get_random_word(word_file="words.txt"):
    # open words.txt
    with open(word_file) as file:
        # file = open(word_file, "r")
        line = next(file)

        # find random word of any length
        for num, aline in enumerate(file, 2):
            if random.randrange(num):
                continue

            line = aline.strip()

        return line


def get_random_5_letter_word(word_file):
    word = get_random_word(word_file)

    # check if word is of length 5
    while len(word) != 5:
        word = get_random_word(word_file)
    else:
        return word


def get_all_5_letter_words(word_file="words.txt"):
    valid_words = []

    try:
        with open(word_file) as file:
            for word in file:
                if len(word.strip()) == 5:
                    valid_words.append(word.strip())

        textfile = open("5_letter_words_file.txt", "w")
        textfile.truncate()

        for element in valid_words:
            textfile.write(element + "\n")

        textfile.close()

        return valid_words
    except FileNotFoundError:
        print("No file found")
        raise


class DictionaryTest(unittest.TestCase):

    def test_dictionary_word_positive(self):
        word = get_random_5_letter_word("test_word_file.txt")
        self.assertEqual(word, "aaron")

    def test_dictionary_word_negative(self):
        word = get_random_5_letter_word("test_word_file.txt")
        self.assertNotEqual(word, "shawn")

    def test_dictionary_word_length_positive(self):
        word = get_random_5_letter_word("test_word_file.txt")
        self.assertEqual(len(word), 5)

    def test_dictionary_get_all_5_letter_words_positive(self):
        with self.assertRaises(FileNotFoundError):
            get_all_5_letter_words("no_file.txt")

    def test_dictionary_get_all_5_letter_words_negative(self):
        with self.assertRaises(ValueError):
            get_all_5_letter_words("no_file.txt")

    def test_dictionary_word_list_positive(self):
        list = ["aaron"]
        words = get_all_5_letter_words("test_word_file.txt")
        self.assertEqual(words, list)

    def test_dictionary_word_list_negative(self):
        list = ["aaron", "bruce"]
        words = get_all_5_letter_words("test_word_file.txt")
        self.assertEqual(words, list)
