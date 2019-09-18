import random


x = int(random.uniform(1, 100))


g = 0


numG = 0

while g != x:

    g = int(input('Take a guess (1-100): '))
    numG += 1


    if g > x:
        print('Your guess was too high! Guess lower.')
    elif g < x:
        print('Your guess was too low! Guess higher.')


print('You finally guessed the number in ' + str(numG) + ' tries.')
