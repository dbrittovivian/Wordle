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
    print(letter_dict)

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

    def test_get_letter_dictionary_positive(self):
        test_dict = {'a': [0.057, 0.167, 0.124, 0.065, 0.037], 'b': [0.078, 0.004, 0.02, 0.015, 0.004], 'c': [0.081, 0.012, 0.028, 0.056, 0.011], 'd': [0.051, 0.01, 0.03, 0.045, 0.064], 'e': [0.029, 0.117, 0.077, 0.182, 0.145], 'f': [0.057, 0.002, 0.006, 0.009, 0.007], 'g': [0.034, 0.004, 0.03, 0.025, 0.012], 'h': [0.031, 0.062, 0.004, 0.014, 0.046], 'i': [0.016, 0.108, 0.096, 0.071, 0.007], 'j': [0.017, 0.0, 0.002, 0.0, 0.0], 'k': [0.017, 0.003, 0.014, 0.03, 0.029], 'l': [0.052, 0.07, 0.07, 0.067, 0.046], 'm': [0.055, 0.012, 0.028, 0.027, 0.013], 'n': [
            0.02, 0.025, 0.084, 0.079, 0.059], 'o': [0.017, 0.155, 0.091, 0.049, 0.027], 'p': [0.057, 0.022, 0.019, 0.02, 0.007], 'q': [0.007, 0.001, 0.0, 0.001, 0.0], 'r': [0.043, 0.097, 0.085, 0.066, 0.067], 's': [0.127, 0.012, 0.035, 0.051, 0.245], 't': [0.075, 0.025, 0.051, 0.071, 0.079], 'u': [0.011, 0.059, 0.048, 0.024, 0.001], 'v': [0.017, 0.004, 0.027, 0.015, 0.0], 'w': [0.04, 0.01, 0.007, 0.009, 0.004], 'x': [0.002, 0.004, 0.01, 0.001, 0.007], 'y': [0.008, 0.01, 0.011, 0.006, 0.082], 'z': [0.001, 0.001, 0.004, 0.004, 0.001]}
        d = get_letter_dictionary()
        self.assertEqual(test_dict, d)

    def test_get_letter_dictionary_negative(self):
        test_dict = {'a': (0.0, 0.167, 0.124, 0.065, 0.037), 'b': (0.0, 0.004, 0.02, 0.015, 0.00), 'c': (0.081, 0.012, 0.028, 0.056, 0.011), 'd': (0.051, 0.01, 0.03, 0.045, 0.064), 'e': (0.029, 0.117, 0.077, 0.182, 0.145), 'f': (0.057, 0.002, 0.006, 0.009, 0.007), 'g': (0.034, 0.004, 0.03, 0.025, 0.012), 'h': (0.031, 0.062, 0.004, 0.014, 0.046), 'i': (0.016, 0.108, 0.096, 0.071, 0.007), 'j': (0.017, 0.0, 0.002, 0.0, 0.0), 'k': (0.017, 0.003, 0.014, 0.03, 0.029), 'l': (0.052, 0.07, 0.07, 0.067, 0.046), 'm': (0.055, 0.012, 0.028, 0.027, 0.013), 'n': (
            0.02, 0.025, 0.084, 0.079, 0.059), 'o': (0.017, 0.155, 0.01, 0.049, 0.027), 'p': (0.057, 0.022, 0.019, 0.02, 0.007), 'q': (0.007, 0.001, 0.0, 0.001, 0.0), 'r': (0.043, 0.097, 0.085, 0.066, 0.067), 's': (0.127, 0.012, 0.035, 0.051, 0.245), 't': (0.075, 0.025, 0.051, 0.071, 0.079), 'u': (0.011, 0.059, 0.048, 0.024, 0.001), 'v': (0.017, 0.004, 0.027, 0.015, 0.0), 'w': (0.04, 0.01, 0.007, 0.009, 0.004), 'x': (0.002, 0.004, 0.01, 0.001, 0.007), 'y': (0.008, 0.01, 0.011, 0.006, 0.082), 'z': (0.001, 0.001, 0.004, 0.004, 0.001)}
        d = get_letter_dictionary()
        self.assertEqual(test_dict, d)

    def test_convert_to_tuples_positive(self):
        test_dict = {'a': (2, 3, 4, 5, 6)}
        tup_dict = convert_to_tuples({'a': [2, 3, 4, 5, 6]})
        self.assertEqual(test_dict, tup_dict)

    def test_convert_to_tuples_negative(self):
        test_dict = {'a': [2, 3, 4, 5, 6]}
        tup_dict = convert_to_tuples({'a': [2, 3, 4, 5, 6]})
        self.assertEqual(test_dict, tup_dict)

    def test_get_dict_from_csv_positive(self):
        test_dict = {'a': (0.057, 0.167, 0.124, 0.065, 0.037), 'b': (0.078, 0.004, 0.02, 0.015, 0.004), 'c': (0.081, 0.012, 0.028, 0.056, 0.011), 'd': (0.051, 0.01, 0.03, 0.045, 0.064), 'e': (0.029, 0.117, 0.077, 0.182, 0.145), 'f': (0.057, 0.002, 0.006, 0.009, 0.007), 'g': (0.034, 0.004, 0.03, 0.025, 0.012), 'h': (0.031, 0.062, 0.004, 0.014, 0.046), 'i': (0.016, 0.108, 0.096, 0.071, 0.007), 'j': (0.017, 0.0, 0.002, 0.0, 0.0), 'k': (0.017, 0.003, 0.014, 0.03, 0.029), 'l': (0.052, 0.07, 0.07, 0.067, 0.046), 'm': (0.055, 0.012, 0.028, 0.027, 0.013), 'n': (
            0.02, 0.025, 0.084, 0.079, 0.059), 'o': (0.017, 0.155, 0.091, 0.049, 0.027), 'p': (0.057, 0.022, 0.019, 0.02, 0.007), 'q': (0.007, 0.001, 0.0, 0.001, 0.0), 'r': (0.043, 0.097, 0.085, 0.066, 0.067), 's': (0.127, 0.012, 0.035, 0.051, 0.245), 't': (0.075, 0.025, 0.051, 0.071, 0.079), 'u': (0.011, 0.059, 0.048, 0.024, 0.001), 'v': (0.017, 0.004, 0.027, 0.015, 0.0), 'w': (0.04, 0.01, 0.007, 0.009, 0.004), 'x': (0.002, 0.004, 0.01, 0.001, 0.007), 'y': (0.008, 0.01, 0.011, 0.006, 0.082), 'z': (0.001, 0.001, 0.004, 0.004, 0.001)}
        csv_dict = get_dict_from_csv()
        self.assertEqual(test_dict, csv_dict)

    def test_get_dict_from_csv_negative(self):
        test_dict = {'a': (0.057, 0.167, 0.124, 0.065, 0.037), 'b': (0.078, 0.004, 0.02, 0.015, 0.004), 'c': (0.081, 0.012, 0.028, 0.056, 0.011), 'd': (0.051, 0.01, 0.03, 0.045, 0.064), 'e': (0.029, 0.117, 0.077, 0.182, 0.145), 'f': (0.057, 0.002, 0.006, 0.009, 0.007), 'g': (0.034, 0.004, 0.03, 0.025, 0.012), 'h': (0.031, 0.062, 0.004, 0.014, 0.046), 'i': (0.016, 0.108, 0.096, 0.071, 0.007), 'j': (0.017, 0.0, 0.002, 0.0, 0.0), 'k': (0.017, 0.003, 0.014, 0.03, 0.029), 'l': (0.052, 0.07, 0.07, 0.067, 0.046), 'm': (0.055, 0.012, 0.028, 0.027, 0.013), 'n': (
            0.02, 0.025, 0.084, 0.079, 0.059), 'o': (0.017, 0.155, 0.091, 0.049, 0.027), 'p': (0.057, 0.022, 0.019, 0.02, 0.007), 'q': (0.007, 0.001, 0.0, 0.001, 0.0), 'r': (0.043, 0.097, 0.085, 0.066, 0.067), 's': (0.127, 0.012, 0.035, 0.051, 0.245), 't': (0.075, 0.025, 0.051, 0.071, 0.079), 'u': (0.011, 0.059, 0.048, 0.024, 0.001), 'v': (0.017, 0.004, 0.027, 0.015, 0.0), 'w': (0.04, 0.01, 0.007, 0.009, 0.004), 'x': (0.002, 0.004, 0.01, 0.001, 0.007), 'y': (0.008, 0.01, 0.011, 0.006, 0.082), 'z': (0.001, 0.001, 0.004, 0.004, 0.001)}
        csv_dict = get_dict_from_csv('no_file.csv')
        self.assertEqual(test_dict, csv_dict)
