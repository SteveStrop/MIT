import unittest
from string import ascii_lowercase

# from credit import min_repay
# from odd_tuples import  oddTuples
# from applyToEach import apply
# from dict_exercises import how_many,biggest
from week3.ps3_hangman import isWordGuessed, getGuessedWord, getAvailableLetters, get_guess,check_guess


class EDX(unittest.TestCase):
    # def test_min_repayment(self):
    #     self.assertIn('29157.09', min_repay(320000, 0.2))
    #     self.assertIn('90325.03', min_repay(999999, 0.18))
    #
    # def test_odd_tuples(self):
    #     self.assertEqual(oddTuples(('I', 'am', 'a', 'test', 'tuple')), ('I', 'a', 'tuple'))
    #
    # def test_apply_to_each(self):
    #     self.assertEqual([2, -3, 9, -8],apply())
    # def test_how_many(self):
    #     self.assertEqual(6,how_many({'u': [10, 15, 5, 2, 6], 'B': [15]}))
    # def test_biggest(self):
    #     self.assertEqual('d',biggest())
    def test_isWordGuessed(self):
        self.assertEqual(False, isWordGuessed('apple', ['e', 'i', 'k', 'p', 'r', 's']))
        self.assertEqual(True, isWordGuessed('apple', ['e', 'a', 'k', 'l', 'r', 'p']))

    def test_getGuessedWord(self):
        self.assertEqual('_ _ _ _ e', getGuessedWord('apple', ['e', 'i', 'k', 'r', 's']))

    def test_getAvailableLetters(self):
        self.assertEqual('abcdfghjlmnoqtuvwxyz', getAvailableLetters(['e', 'i', 'k', 'p', 'r', 's']))

    def test_get_guess(self):
        letter_list = ascii_lowercase.replace('a','')
        self.assertIn(get_guess(letter_list),'a')
    def test_check_guess(self):
        self.assertEqual(7,check_guess('a','frog',8)[0])
        self.assertIn('Good', check_guess('o', 'frog', 8)[1])
        self.assertIn('Oops!', check_guess('a', 'frog', 8)[1])
