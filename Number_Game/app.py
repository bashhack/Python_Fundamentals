import random

# generate rand num between 1 and 10
rand_num = random.randint(1, 10)

while True:
    # get player input (guess)
    guess = int(input('Guess a number between 1 and 10: '))
    # compare guess against generated num
    # print hit/miss
    if guess == rand_num:
        print('My number was {}.'.format(rand_num))
        break
    else:
        print('Guess again!')
