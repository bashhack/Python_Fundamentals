'''
Letter guessing game a la Hangman
'''
import random

# Make a list of words
words = [
    'osx',
    'windows',
    'fedora',
    'ubuntu',
    'gnome',
    'kali'
]

while True:
    start = input('Press enter/return to start, or enter Q to quit.')
    if start.lower() == 'q':
        break

    # Pick a random word
    rand_word = random.choice(words)
    bad_guesses = []
    good_guesses = []

    while len(bad_guesses) < 7 and len(good_guesses) != len(list(rand_word)):
        # Draw spaces
        for letter in rand_word:
            if letter in good_guesses:
                print(letter, end='')
            else:
                print('_', end='')

        print('')
        print('Strikes: {}/7'.format(len(bad_guesses)))
        print('')

        # Take a guess
        guess = input('Guess a letter: ').lower()

        if len(guess) != 1:
            print('You can only guess a single letter!')
            continue
        elif guess in bad_guesses or guess in good_guesses:
            print('You have already guessed that letter!')
            continue
        elif not guess.isalpha():
            print('You can only guess letters.')
            continue

        if guess in rand_word:
            good_guesses.append(guess)
            if len(good_guesses) == len(list(rand_word)):
                print('You win! The word was {}.'.format(rand_word))
                break
        else:
            bad_guesses.append(guess)
    else:
        print('You lose - my secret word was {}'.format(rand_word))
