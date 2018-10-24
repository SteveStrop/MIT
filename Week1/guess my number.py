print('Please think of a number between 0 and 100!')
low = 0
high = 100
while True:
    my_guess = int((high + low) / 2)
    print('Is your secret number', my_guess, '?')
    user_response = input(
            "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to "
            "indicate I guessed correctly.")
    if user_response not in 'hlc':
        print("Sorry, I did not understand your input.")

    elif user_response == 'h':
        high = my_guess
    elif user_response == 'l':
        low = my_guess
    else:
        print('Game over. Your secret number was:', my_guess)
        break


def dummy(first, second):
    """Return the concatenation of first and second with a space between.

    :arg first (string)
    :arg second (string)
    :returns (string)"""
    return first + ' ' + second


dummy
