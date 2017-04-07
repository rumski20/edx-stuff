# unit 2 | lecture 5 | exercise 5
import random


def roll_foursided():
    """returns a random int between 1 and 6"""
    return random.choice([1, 2, 3, 4])


def even_sim(num_trials):
    """
    simulate probability of rolling an even number
    :param num_trials: 
    :return: probability
    """
    return len([t for t in range(num_trials) if roll_foursided() % 2 == 0]) \
           / num_trials

# print('Frequency of even number',
#       str(even_sim(100000) * 100) + '%')

def two_followedby_three(num_trials):
    """
    simulate the probability of rolling a two followed by a three
    :param num_trials: 
    :return: probability
    """
    count = 0
    for t in range(num_trials):
        if roll_foursided() == 2:
            if roll_foursided() == 3:
                count += 1
    return count / num_trials

# print('Frequency of two followed by three',
#       str(two_followedby_three(1000000) * 100) + '%')


def two_and_three(num_trials):
    """
    simulate the probability of rolling a two and a three
    :param num_trials: 
    :return: probability
    """
    return len([t for t in range(num_trials)
                if (roll_foursided(), roll_foursided())
                in [(2, 3), (3, 2)]]) \
           / num_trials

# print('Frequency of two and a three',
#       str(two_and_three(1000000) * 100) + '%')


def first_equal_second(num_trials):
    """
    simulate the probability of rolling a two and a three
    :param num_trials: 
    :return: probability
    """
    return len([t for t in range(num_trials)
                if roll_foursided() == roll_foursided()]) / num_trials

# print('Frequency of first equals second',
#       str(first_equal_second(1000000) * 100) + '%')

def atleast_a_four(num_trials):
    """
    simulate the probability of rolling a two and a three
    :param num_trials: 
    :return: probability
    """
    return len([t for t in range(num_trials)
                if roll_foursided() == 4 or roll_foursided() == 4])\
                / num_trials

# print('Frequency of at least a four',
#       str(atleast_a_four(10000000) * 100) + '%')

def no_fours(num_trials):
    """
    simulate the probability of rolling a two and a three
    :param num_trials: 
    :return: probability
    """
    return len([t for t in range(num_trials)
                if roll_foursided() != 4 and roll_foursided() != 4])\
                / num_trials

# print('Frequency of no fours',
#       str(no_fours(1000000) * 100) + '%')

def first_larger_than_second(num_trials):
    """
    simulate the probability of rolling a two and a three
    :param num_trials: 
    :return: probability
    """
    return len([t for t in range(num_trials)
                if roll_foursided() > roll_foursided()])\
                / num_trials

print('Frequency of first roll larger than second',
      str(first_larger_than_second(1000000) * 100) + '%')
