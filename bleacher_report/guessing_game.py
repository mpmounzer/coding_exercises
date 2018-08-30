# Marc Mounzer's guessing_game.py for Bleacher Report
# 8/24/2018

import random

def play_guessing_game():
    num_guesses = 0

    random_number = random.randint(1,100)

    while(True):
        user_guess = input('Guess a number from 1 to 100: ')

        # invalid guesses won't be counted toward the guess total
        if not user_guess.isnumeric():
            print('Please guess a number from 1 to 100')
            continue

        # if the guess is a number, convert it to an int
        user_guess = int(user_guess)
        if user_guess < 1 or user_guess > 100:
            print('Please guess a number from 1 to 100')
            continue

        num_guesses = num_guesses + 1

        # the difference between the guess and the actual number will determine what we do next
        guess_result = user_guess - random_number

        # if the difference is 0, the guess was correct
        if guess_result == 0:
            print(f'You guessed correctly!  It took you {num_guesses} guesses')
            break
        else:
            # if the difference is positive, the guess was too high
            if guess_result > 0:
                print('Your guess was too high!')
            # if the difference is negative, the guess was too low
            elif guess_result < 0:
                print('Your guess was too low!')

# shall we play a game?
while(True):
    want_to_play = input('Would you like to play the guessing game? Y/N: ')

    if(want_to_play[0].lower() == 'y'):
        play_guessing_game()
    else:
        print('Ok, bye!')
        break