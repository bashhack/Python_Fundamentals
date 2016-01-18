import random
import os


# print result
def print_rand_num(num):
    '''Print value of rand_num variable to user'''
    print('My number was {}.'.format(num))


# main game logic
def game():
    # generate rand num between 1 and 10
    rand_num = random.randint(1, 10)

    guesses = []

    while len(guesses) < 4:
        # get player input (guess)
        guess = input('Guess a number between 1 and 10: ')
        try:
            guess = int(guess)
        except ValueError:
            print('"{}" is not a valid integer.'.format(guess))
            guesses.append(guess)
        else:
            # compare guess against generated num
            # print hit/miss
            if guess == rand_num:
                print('You got it!')
                print('My number was {}.'.format(rand_num))
                break
            elif guess > rand_num:
                print('Too high!')
                guesses.append(guess)
            elif guess < rand_num:
                print('Too low!')
                guesses.append(guess)

    else:
        print('You\'ve run out of guesses!')
        print_rand_num(rand_num)

    new_game = str(input('Would you like to play again? ' +
                   'Type \'Y\' or \'N\': '))
    if new_game.upper() == 'Y':
        os.system('cls' if os.name == 'nt' else 'clear')
        game()
    else:
        print('Thanks for playing!')

game()
