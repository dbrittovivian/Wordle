import unittest


def validate_word(EXPECTED_WORD, input_word):
    letter_counts: dict = {}
    appraisal = []

    # sort word in dictionary by letters
    for letter in EXPECTED_WORD:
        if letter in letter_counts.keys():
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1

    # validate if letter is present or missing
    for index in range(len(EXPECTED_WORD)):
        if input_word[index] == EXPECTED_WORD[index]:
            appraisal.append(' ')
            letter_counts[EXPECTED_WORD[index]] -= 1
        else:
            appraisal.append('"')

    # check if existing letter is placed in wrong position
    for index in range(len(EXPECTED_WORD)):
        if input_word[index] != EXPECTED_WORD[index]:
            if input_word[index] in letter_counts:
                if letter_counts[input_word[index]] > 0:
                    letter_counts[input_word[index]] -= 1
                    appraisal[index] = "`"

    return ''.join(appraisal)


class WordleTest(unittest.TestCase):

    def test_wordle_positive(self):
        word = validate_word("AARON", "AAAAA")
        self.assertEqual(word, '  """')

    def test_wordle_negative(self):
        word = validate_word("AARON", "AAAAA")
        self.assertNotEqual(word, '   ""')

    def test_wordle_match_positive(self):
        word = validate_word("AARON", "AARON")
        self.assertEqual(word, '     ')

    def test_wordle_match_negative(self):
        word = validate_word("AARON", "AARON")
        self.assertNotEqual(word, '""   ')

    def test_wordle_incorrect_positive(self):
        word = validate_word("AARON", "RNAAA")
        self.assertEqual(word, '````"')

    def test_wordle_incorrect_negative(self):
        word = validate_word("AARON", "RNAAA")
        self.assertNotEqual(word, '"```"')
