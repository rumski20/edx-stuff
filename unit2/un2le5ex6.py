# unit 2 | lecture 5 | exercise 6
import random


def roll_tensided():
    """returns a random int between 1 and 6"""
    return random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

def roll_8sided():
    """returns a random int between 1 and 6"""
    return random.choice([1, 2, 3, 4, 5, 6, 7, 8])


def even_sim(num_trials):
    """
    simulate probability of rolling an even number
    :param num_trials: 
    :return: probability
    """
    return len([t for t in range(num_trials) if roll_tensided() % 2 == 0]) \
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
        if roll_tensided() == 2:
            if roll_tensided() == 3:
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
                if (roll_tensided(), roll_tensided())
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
                if roll_tensided() == roll_tensided()]) / num_trials


# print('Frequency of first equals second',
#       str(first_equal_second(1000000) * 100) + '%')

def atleast_a_four(num_trials):
    """
    simulate the probability of rolling a two and a three
    :param num_trials: 
    :return: probability
    """
    return len([t for t in range(num_trials)
                if roll_tensided() == 4 or roll_tensided() == 4]) \
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
                if roll_tensided() != 4 and roll_tensided() != 4]) \
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
                if roll_tensided() > roll_tensided()]) \
           / num_trials


# print('Frequency of first roll larger than second',
#       str(first_larger_than_second(1000000) * 100) + '%')

def first_equal_second_equals_third(num_trials):
    """
    simulate the probability of rolling a two and a three
    :param num_trials: 
    :return: probability
    """
    return len([t for t in range(num_trials)
                if roll_8sided() == roll_8sided() == roll_8sided()]) \
                / num_trials


print('Frequency of first equals second equals third',
      str(first_equal_second_equals_third(10000000) * 100) + '%')
