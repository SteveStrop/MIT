from string import ascii_lowercase
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program

def isWordGuessed(secret_word, lettersGuessed):
    '''
    secret_word: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secret_word are in lettersGuessed;
      False otherwise
    '''

    # FILL IN YOUR CODE HERE...
    # get unique letters in secret word
    secret_word = set(list(secret_word))
    for letter in secret_word:
        if letter not in lettersGuessed:
            return False
    return True


def getGuessedWord(secret_word, lettersGuessed):
    '''
    secret_word: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    word = ''.join(letter if letter in lettersGuessed else '_' for letter in secret_word)
    while '__' in word:
        word = word.replace('__', '_ _')
    return word


def getAvailableLetters(letters_guessed):
    '''
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    return ''.join(letter for letter in ascii_lowercase if letter not in letters_guessed)


def intro(secret_word):
    print('Welcome to the game, Hangman!')
    print(f'I am thinking of a word {len(secret_word)} letters long.')
    return


def get_guess(letters_guessed):
    """ return a lower case letter that has not been guessed so far"""
    while True:
        print('Please guess a letter: ', end='')
        while True:
            guess = input().lower()
            # non alpha input
            if not guess.isalpha():
                err_msg = f'{guess} is not a letter .'
            # already guessed that letter
            elif guess in letters_guessed:
                err_msg = f"You've already guessed {guess} ."
            # no errors
            else:
                letters_guessed.append(guess)
                return guess

            print(err_msg, 'Try again: ', end='')


def check_guess(guess, secret_word, guesses):
    if guess in secret_word:
        string = f'Good guess: '
    else:
        guesses -= 1
        string = f'Oops! That letter is not in my word :'
    return guesses, string


def hangman_round(secret_word, guesses, lettersGuessed):
    print('-----------')
    print(f"Guesses left: {guesses}")
    print(f"Available letters: {getAvailableLetters(lettersGuessed)}")
    guess = get_guess(lettersGuessed)
    guesses, guess_type = check_guess(guess, secret_word, guesses)
    return guesses, f"{guess_type} {getGuessedWord(secret_word,lettersGuessed)}"


def hangman(secret_word):
    """
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    """
    # FILL IN YOUR CODE HERE...

    guesses = 8
    letters_guessed = []
    intro(secret_word)

    while True:
        guesses, result = hangman_round(secret_word, guesses, letters_guessed)
        print(result)
        if guesses == 0:
            return f"Game over numpty. My secret word was: {secret_word}"
        elif isWordGuessed(secret_word, letters_guessed):
            return 'Winner'


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)
if __name__ == "__main__":
    print(hangman(chooseWord(loadWords()).lower()))
