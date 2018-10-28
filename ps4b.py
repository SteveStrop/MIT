from ps4a import *
import time


#
#
# Computer chooses a word
#
#
def compChooseWord(hand, word_dict):
    """
    Given a hand and a wordList, find the word that gives
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    # Create a new variable to store the maximum score seen so far (initially 0)
    bestScore = 0
    # Create a new variable to store the best word seen so far (initially None)
    bestWord = None
    # For each word in the wordList
    for word in word_dict.keys():
        # If you can construct the word from your hand
        if isValidWord(word, hand, word_dict.keys()):
            # find out how much making that word is worth
            score = word_dict[word]
            # If the score for that word is higher than your best score
            if (score > bestScore):
                # update your best score, and best word accordingly
                bestScore = score
                bestWord = word
                # print(f"best score so far is: {bestScore} for {bestWord}")
    # return the best word you found.
    return bestWord


#
# Computer plays a hand
#
def compPlayHand(hand, word_dict):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is
    displayed, the remaining letters in the hand are displayed, and the
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    # Keep track of the total score
    totalScore = 0
    # As long as there are still letters left in the hand:
    while (calculateHandlen(hand) > 0):
        # Display the hand
        print("Current Hand: ", end=' ')
        displayHand(hand)
        # computer's word
        word = compChooseWord(hand, word_dict)
        # If the input is a single period:
        if word is None:
            # End the game (break out of the loop)
            break

        # Otherwise (the input is not a single period):
        else:
            # If the word is not valid:
            if not isValidWord(word, hand, wordList):
                print('This is a terrible error! I need to check my own code!')
                break
            # Otherwise (the word is valid):
            else:
                # Tell the user how many points the word earned, and the updated total score
                score = word_dict[word]
                totalScore += score
                print('"' + word + '" earned ' + str(score) + ' points. Total: ' + str(totalScore) + ' points')
                # Update hand and show the updated hand to the user
                hand = updateHand(hand, word)
                print()
    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    print('Total score: ' + str(totalScore) + ' points.')
    return totalScore


def get_user_input(prompt="", retry_prompt="", valid_check=""):
    """ Prompt user for input. Normalise input to lower case.
    Check given input against valid_check and re prompts with retry_prompt if user input is not valid.
    Repeat unit user gives valid input
    :param prompt: a string displayed to the user
    :param valid_check: a string containing all valid inputs normalised to lower case
    :param retry_prompt: a string displayed to the user if input is invalid
    :returns a string containing valid input normalised to lower case"""
    print(prompt, end=" ")
    while True:
        user_input = input().lower()
        if user_input and user_input in valid_check:
            return user_input
        print(retry_prompt, end=" ")


#
# Problem #6: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.

        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    # initialise hand length (number of letter dealt to each player)
    n = 7
    #  initialise dictionary of functions to call for user and computer players
    player_func = {'comp': compPlayHand, 'user': playHand}
    # initialise user and computer scores
    score = {'comp': 0, 'user': 0}
    # create dictionary of word scores to speed up computer player searches
    word_dict = {word: getWordScore(word, n) for word in wordList}
    # get a starting hand
    # play the game until user hits e to exit
    # while True:
    #     player_response = get_user_input(
    #         prompt="Type (n)ew hand, (r)eplay the last hand, or (e)xit",
    #         valid_check="nre",
    #         retry_prompt="Sorry I didn't get that. Try again with n, r, or e."
    #     )
    #     if player_response == 'e':
    #         return f"Bye!\nYour final score is {score['u']}\nComputer's score is {score['c']}"
    #     player = get_user_input(  # either (u)ser or(c)omputer
    #         prompt="Who's go is it (u)ser or (c)omputer: ",
    #         valid_check="uc",
    #         retry_prompt="Sorry I didn't get that. Try again with u or c."
    #     )
    #     # new hand
    #     if player_response == 'n':
    #         old_hand = hand.copy()
    #         score[player] += player_func[player](hand, word_dict, n)
    #         # generate new hand for NEXT round
    #         hand = dealHand(n)
    #     # replay hand
    #     elif player_response == 'r':
    #         score[player] += player_func[player](old_hand, word_dict, n)
    while True:
        player_response = get_user_input(
            prompt="Type (n)ew hand or (e)xit",
            valid_check="ne",
            retry_prompt="Sorry I didn't get that. Try again with n or e."
        )
        if player_response == 'e':
            return f"Bye!\nYour final score is {score['user']}\nComputer's score is {score['comp']}"
        # get new hand for this round
        hand = dealHand(n)
        # play user hand
        print("\n"*5,"-" * 25, "YOUR TURN", "-" * 25, sep="")
        score['user'] += player_func['user'](hand, word_dict, n)
        # play computer hand
        print("-"*25,"COMPUTER'S TURN","-"*25,sep="")
        score['comp'] += player_func['comp'](hand, word_dict)


#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()

    print(playGame(wordList))
