'''
Letter guessing game a la Hangman
'''
import random
import os
import sys

# Make a list of words
words = [
    'osx',
    'windows',
    'fedora',
    'ubuntu',
    'gnome',
    'kali'
]


# Clear console
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def draw(bad_guesses, good_guesses, rand_word):
    clear()

    print('Strikes: {}/7'.format(len(bad_guesses)))
    print('')

    for letter in bad_guesses:
        print(letter, end=' ')
    print('\n\n')

    # Draw spaces
    for letter in rand_word:
        if letter in good_guesses:
            print(letter, end='')
        else:
            print('_', end='')

    print('')


def get_guess(bad_guesses, good_guesses):
    while True:
        # Get user input
        guess = input('Guess a letter: ').lower()

        if len(guess) != 1:
            print('You can only guess a single letter!')
        elif guess in bad_guesses or guess in good_guesses:
            print('You have already guessed that letter!')
        elif not guess.isalpha():
            print('You can only guess letters.')
        else:
            return guess


def play_game(done):
    clear()
    rand_word = random.choice(words)
    bad_guesses = []
    good_guesses = []

    while True:
        draw(bad_guesses, good_guesses, rand_word)
        guess = get_guess(bad_guesses, good_guesses)

        if guess in rand_word:
            good_guesses.append(guess)
            found = True
            for letter in rand_word:
                if letter not in good_guesses:
                    found = False
            if found:
                print('You win!')
                print('The secret word was {}'.format(rand_word))
                done = True
        else:
            bad_guesses.append(guess)
            if len(bad_guesses) == 7:
                draw(bad_guesses, good_guesses, rand_word)
                print('You lost!')
                print('The secret word was {}'.format(rand_word))
                done = True

        if done:
            play_again = input('Play again? Y/n ').lower()
            if play_again != 'n':
                return play_game(done=False)
            else:
                sys.exit()


def welcome():
    start = input('Press enter/return to start, or enter Q to quit. ')
    if start.lower() == 'q':
        print('Goodbye - thanks for playing!')
        sys.exit()
    else:
        return True

print('Welcome to the letter game!')

done = False

while True:
    clear()
    welcome()
    play_game(done)
