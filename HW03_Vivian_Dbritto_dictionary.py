from asyncio.windows_events import NULL
import random
import string
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


def get_letter_dictionary(file="letterFrequency.csv"):
    letter_dict = {}

    [letter_dict.setdefault(x, [0, 0, 0, 0, 0])
     for x in string.ascii_lowercase]

    words = get_all_5_letter_words()

    for word in words:
        for i in range(len(word)):
            letter = word[i]
            list = letter_dict.get(letter)
            list[i] += 1
            letter_dict[letter] = list

    letter_dict = get_letter_stats(letter_dict, len(words))

    textfile = open(file, "w")
    textfile.truncate()

    for key in letter_dict:
        count_list = letter_dict.get(key)
        textfile.write(
            f'{key}, {count_list[0]}, {count_list[1]}, {count_list[2]}, {count_list[3]}, {count_list[4]}\n')

    textfile.close()

    return letter_dict


def get_letter_stats(letter_dict, words_count):

    for key in letter_dict:
        count_list = letter_dict.get(key)

        for i in range(len(count_list)):
            count = round(count_list[i] / words_count, 3)
            count_list[i] = count

        letter_dict[key] = count_list

    return letter_dict


def convert_to_tuples(dictionary={}):
    for key in dictionary:
        count_list = dictionary.get(key)
        count_tuple = tuple(count_list)
        dictionary[key] = count_tuple

    return dictionary


def get_dict_from_csv(csv_file="letterFrequency.csv"):
    d = {}

    try:
        with open(csv_file) as f:
            for line in f:
                line = line.strip('\n')
                (key, val1, val2, val3, val4, val5) = line.split(", ")
                d[key] = (float(val1), float(val2), float(
                    val3), float(val4), float(val5))

        print(d)
    except FileNotFoundError:
        print("No file found")
        raise

    return d


def get_words_probability(file="wordRank.csv"):
    words = get_all_5_letter_words()
    letter_dict = get_dict_from_csv()
    word_prob = {}

    for word in words:
        prob = 1
        for i in range(len(word)):
            letter = word[i]
            list = letter_dict.get(letter)
            prob *= list[i]

        word_prob.update({word: prob})

    sorted_list = sorted(word_prob.items(), key=lambda x: x[1], reverse=1)

    textfile = open(file, "w")
    textfile.truncate()

    i = 1
    for element in sorted_list:
        textfile.write(f'{i}, {element[0]}, {element[1]}\n')
        i += 1

    textfile.close


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
