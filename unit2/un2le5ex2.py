# unit 2 | lecture 5 | exercise 2

import random


def genEven():
    '''
    Returns a random even number x, where 0 <= x < 100
    '''
    return random.randrange(0, 100, 2)


def deterministicNumber():
    '''
    Deterministically generates and returns an even number between 9 and 21
    '''
    return 16

def stochasticNumber():
    '''
    Stochastically generates and returns a uniformly distributed even number between 9 and 21
    '''
    # Your code here
    # ref: http://stackoverflow.com/a/2184774/6072959
    evenlist = [x for x in range(9, 21) if x % 2 == 0]
    return random.choice(evenlist)


# TESTING

# print('Testing getEven:')
# for n in range(10): print(genEven())

print('Testing deterministicNumber:')
for n in range(10): print(deterministicNumber())
