import random

def func(numG=0,target=42):
    g = int(input('Take a guess (1-100): '))
    numG += 1


    if g > target:
        print('Your guess was too high! Guess lower.')
    elif g < target:
        print('Your guess was too low! Guess higher.')
    else:
        print('You finally guessed the number in ' + str(numG) + ' tries.')
        return
    func(numG,target)


func(target=int(random.uniform(1, 100)))




   


