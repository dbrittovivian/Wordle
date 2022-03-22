import unittest
from HW03_Vivian_Dbritto_ui import Ui as ui
from HW03_Vivian_Dbritto_wordle import Wordle as wordle
from HW03_Vivian_Dbritto_dictionary import Dictionary as dictionary
from HW03_Vivian_Dbritto_letterfrequency import frequency as frequency
from unittest.mock import patch


class WordleTest(unittest.TestCase):

    @patch('builtins.input', side_effect=["weeks"])
    def test_user_input_length_positive(self, mock_inputs) -> None:
        """Test when the input length is correct"""
        uitest = ui()
        self.assertEqual(len(uitest.userinput(1)), 5)

    @patch('builtins.input', side_effect=["burger"])
    def test_user_input_length_negative(self, mock_inputs) -> None:
        """Test when the input length is not correct"""
        uitest = ui()
        self.assertNotEqual(len(uitest.userinput(1)), 5)

    @patch('builtins.input', side_effect=["walks"])
    def test_user_input_valid_dictionary_word_positive(self, mock_inputs) -> None:
        """Test when the input word is a valid dictionary word"""
        dicttest = dictionary()
        uitest = ui()
        self.assertTrue(dicttest.checkWord(uitest.userinput(1)))

    @patch('builtins.input', side_effect=["craft"])
    def test_user_input_no_special_characters(self, mock_inputs) -> None:
        """Test when the input does not contain any special characters"""
        uitest = ui()
        self.assertTrue(uitest.userinput(1))

    def test_compare_word_function_positive(self) -> None:
        """Testing the compare function with correct inputs"""
        wordletest = wordle()
        self.assertTrue(wordletest.compareWord("Zones", "Zones"))

    def test_compare_word_function_negative(self) -> None:
        """Testing the compare function with incorrect inputs"""
        wordletest = wordle()
        self.assertFalse(wordletest.compareWord("Zones", "Looks"))

    def test_quit_function_positive(self) -> None:
        """Testing the quit function with empty string"""
        uitest = ui()
        self.assertTrue(uitest.quitfunction(""))

    def test_quit_function_negative(self) -> None:
        """Testing the quit function with a valid word"""
        uitest = ui()
        self.assertFalse(uitest.quitfunction("Books"))

    def test_file_size_function(self) -> None:
        """Testing file size function"""
        dicttest = dictionary()
        self.assertFalse(dicttest.fileSize())

    def test_check_temp_function_positive(self) -> None:
        """Testing checkTemp function with temp as not 0"""
        frequencyltest = frequency()
        self.assertTrue(frequencyltest.checkTemp(["A", (3, 5, 7, 2, 3)]))

    def test_check_temp_function_negative(self) -> None:
        """Testing checkTemp function with temp as 0"""
        frequencyltest = frequency()
        self.assertFalse(frequencyltest.checkTemp([""]))


if __name__ == "__main__":
    unittest.main()
