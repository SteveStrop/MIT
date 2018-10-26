import unittest
import random
from string import ascii_lowercase

# from credit import min_repay
# from odd_tuples import  oddTuples
# from applyToEach import apply
# from dict_exercises import how_many,biggest
from week3.ps3_hangman import isWordGuessed, getGuessedWord, getAvailableLetters, get_guess, check_guess

# class EDX(unittest.TestCase):
#     # def test_min_repayment(self):
#     #     self.assertIn('29157.09', min_repay(320000, 0.2))
#     #     self.assertIn('90325.03', min_repay(999999, 0.18))
#     #
#     # def test_odd_tuples(self):
#     #     self.assertEqual(oddTuples(('I', 'am', 'a', 'test', 'tuple')), ('I', 'a', 'tuple'))
#     #
#     # def test_apply_to_each(self):
#     #     self.assertEqual([2, -3, 9, -8],apply())
#     # def test_how_many(self):
#     #     self.assertEqual(6,how_many({'u': [10, 15, 5, 2, 6], 'B': [15]}))
#     # def test_biggest(self):
#     #     self.assertEqual('d',biggest())
#     def test_isWordGuessed(self):
#         self.assertEqual(False, isWordGuessed('apple', ['e', 'i', 'k', 'p', 'r', 's']))
#         self.assertEqual(True, isWordGuessed('apple', ['e', 'a', 'k', 'l', 'r', 'p']))
#
#     def test_getGuessedWord(self):
#         self.assertEqual('_ _ _ _ e', getGuessedWord('apple', ['e', 'i', 'k', 'r', 's']))
#
#     def test_getAvailableLetters(self):
#         self.assertEqual('abcdfghjlmnoqtuvwxyz', getAvailableLetters(['e', 'i', 'k', 'p', 'r', 's']))
#
#     def test_get_guess(self):
#         letter_list = ascii_lowercase.replace('a','')
#         self.assertIn(get_guess(letter_list),'a')
#     def test_check_guess(self):
#         self.assertEqual(7,check_guess('a','frog',8)[0])
#         self.assertIn('Good', check_guess('o', 'frog', 8)[1])
#         self.assertIn('Oops!', check_guess('a', 'frog', 8)[1])
from ps4a import getWordScore, dealHand, VOWELS, updateHand, isValidWord,getFrequencyDict,loadWords


class Ps4aTest(unittest.TestCase):
    def test_getWordScore(self):
        """
        Unit test for getWordScore
        """
        failure = False
        # dictionary of words and scores
        words = {
            ("", 7): 0,
            ("it", 7): 4,
            ("was", 7): 18,
            ("scored", 7): 54,
            ("outgnaw", 7): 127,
            ("fork", 7): 44,
            ("bawn",7) : 36,
            ("fork", 4): 94
        }
        for (word, n) in words.keys():
            try:
                self.assertEqual(words[(word, n)], getWordScore(word, n))
            except AssertionError as err:
                print("FAILURE: test_getWordScore()")
                print("\tExpected", words[(word, n)],
                      "points but got '" + err.__dict__['actual'] + "' for word '" + word + "', n=" + str(n))
                failure = True
        if not failure:
            print("SUCCESS: test_getWordScore()")

    def test_dealHand(self):
        failure = False
        for _ in range(10):
            n = random.randint(0, 50)
            hand = dealHand(n)
            vowel_count = sum(hand[letter] for letter in hand if letter in VOWELS)
            try:
                self.assertGreaterEqual(vowel_count, round(len(hand) / 3))
            except AssertionError as err:
                print("FAILURE: test_dealHand()")
                print("\tExpected", err.__dict__['expected'], "vowels but got ", err.__dict__['actual'], "for a hand",
                      n, "long")
                failure = True
        if not failure:
            print("SUCCESS: test_dealHand()")

    def test_updateHand(self):
        """
        Unit test for updateHand
        """
        # test 1
        handOrig = {'a': 1, 'q': 1, 'l': 2, 'm': 1, 'u': 1, 'i': 1}
        handCopy = handOrig.copy()
        word = "quail"

        hand2 = updateHand(handCopy, word)
        expectedHand1 = {'l': 1, 'm': 1}
        expectedHand2 = {'a': 0, 'q': 0, 'l': 1, 'm': 1, 'u': 0, 'i': 0}
        if hand2 != expectedHand1 and hand2 != expectedHand2:
            print("FAILURE: test_updateHand('" + word + "', " + str(handOrig) + ")")
            print("\tReturned: ", hand2, "\n\t-- but expected:", expectedHand1, "or", expectedHand2)

            return  # exit function
        if handCopy != handOrig:
            print("FAILURE: test_updateHand('" + word + "', " + str(handOrig) + ")")
            print("\tOriginal hand was", handOrig)
            print("\tbut implementation of updateHand mutated the original hand!")
            print("\tNow the hand looks like this:", handCopy)

            return  # exit function

        # test 2
        handOrig = {'e': 1, 'v': 2, 'n': 1, 'i': 1, 'l': 2}
        handCopy = handOrig.copy()
        word = "evil"

        hand2 = updateHand(handCopy, word)
        expectedHand1 = {'v': 1, 'n': 1, 'l': 1}
        expectedHand2 = {'e': 0, 'v': 1, 'n': 1, 'i': 0, 'l': 1}
        if hand2 != expectedHand1 and hand2 != expectedHand2:
            print("FAILURE: test_updateHand('" + word + "', " + str(handOrig) + ")")
            print("\tReturned: ", hand2, "\n\t-- but expected:", expectedHand1, "or", expectedHand2)

            return  # exit function

        if handCopy != handOrig:
            print("FAILURE: test_updateHand('" + word + "', " + str(handOrig) + ")")
            print("\tOriginal hand was", handOrig)
            print("\tbut implementation of updateHand mutated the original hand!")
            print("\tNow the hand looks like this:", handCopy)

            return  # exit function

        # test 3
        handOrig = {'h': 1, 'e': 1, 'l': 2, 'o': 1}
        handCopy = handOrig.copy()
        word = "hello"

        hand2 = updateHand(handCopy, word)
        expectedHand1 = {}
        expectedHand2 = {'h': 0, 'e': 0, 'l': 0, 'o': 0}
        if hand2 != expectedHand1 and hand2 != expectedHand2:
            print("FAILURE: test_updateHand('" + word + "', " + str(handOrig) + ")")
            print("\tReturned: ", hand2, "\n\t-- but expected:", expectedHand1, "or", expectedHand2)

            return  # exit function

        if handCopy != handOrig:
            print("FAILURE: test_updateHand('" + word + "', " + str(handOrig) + ")")
            print("\tOriginal hand was", handOrig)
            print("\tbut implementation of updateHand mutated the original hand!")
            print("\tNow the hand looks like this:", handCopy)

            return  # exit function

        print("SUCCESS: test_updateHand()")

    def test_isValidWord(self):
        """
        Unit test for isValidWord
        """
        failure = False
        wordList = loadWords()
        # test 1
        word = "hello"
        handOrig = getFrequencyDict(word)
        handCopy = handOrig.copy()

        if not isValidWord(word, handCopy, wordList):
            print("FAILURE: test_isValidWord()")
            print("\tExpected True, but got False for word: '" + word + "' and hand:", handOrig)

            failure = True

        # Test a second time to see if wordList or hand has been modified
        if not isValidWord(word, handCopy, wordList):
            print("FAILURE: test_isValidWord()")

            if handCopy != handOrig:
                print("\tTesting word", word, "for a second time - be sure you're not modifying hand.")
                print("\tAt this point, hand ought to be", handOrig, "but it is", handCopy)

            else:
                print("\tTesting word", word, "for a second time - have you modified wordList?")
                wordInWL = word in wordList
                print("The word", word, "should be in wordList - is it?", wordInWL)

            print("\tExpected True, but got False for word: '" + word + "' and hand:", handCopy)

            failure = True

        # test 2
        hand = {'r': 1, 'a': 3, 'p': 2, 'e': 1, 't': 1, 'u': 1}
        word = "rapture"

        if isValidWord(word, hand, wordList):
            print("FAILURE: test_isValidWord()")
            print("\tExpected False, but got True for word: '" + word + "' and hand:", hand)

            failure = True

            # test 3
        hand = {'n': 1, 'h': 1, 'o': 1, 'y': 1, 'd': 1, 'w': 1, 'e': 2}
        word = "honey"

        if not isValidWord(word, hand, wordList):
            print("FAILURE: test_isValidWord()")
            print("\tExpected True, but got False for word: '" + word + "' and hand:", hand)

            failure = True

            # test 4
        hand = {'r': 1, 'a': 3, 'p': 2, 't': 1, 'u': 2}
        word = "honey"

        if isValidWord(word, hand, wordList):
            print("FAILURE: test_isValidWord()")
            print("\tExpected False, but got True for word: '" + word + "' and hand:", hand)

            failure = True

        # test 5
        hand = {'e': 1, 'v': 2, 'n': 1, 'i': 1, 'l': 2}
        word = "evil"

        if not isValidWord(word, hand, wordList):
            print("FAILURE: test_isValidWord()")
            print("\tExpected True, but got False for word: '" + word + "' and hand:", hand)

            failure = True

        # test 6
        word = "even"

        if isValidWord(word, hand, wordList):
            print("FAILURE: test_isValidWord()")
            print("\tExpected False, but got True for word: '" + word + "' and hand:", hand)
            print("\t(If this is the only failure, make sure isValidWord() isn't mutating its inputs)")

            failure = True

        if not failure:
            print("SUCCESS: test_isValidWord()")
