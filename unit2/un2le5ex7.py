# unit 2 | lecture 5 | exercise 7
import random


def ball_bucket():
    """returns a random int between 1 and 6"""
    return random.choice(['R','G'])

def roll_8sided():
    """returns a random int between 1 and 6"""
    return random.choice([1, 2, 3, 4, 5, 6, 7, 8])


def tworeds_onegreen(num_trials):
    """
    simulate probability of rolling an even number
    :param num_trials: 
    :return: probability
    """
    count = 0
    for t in range(num_trials):
        result = [b() for b in [ball_bucket]*3]
        if result.count('R') == 2 and result.count('G') == 1:
            count += 1
    return count / num_trials


# print('Frequency of two reds, one green',
#       str(tworeds_onegreen(100000) * 100) + '%')

def more_reds(num_trials):
    """
    simulate probability of rolling an even number
    :param num_trials: 
    :return: probability
    """
    count = 0
    for t in range(num_trials):
        result = [b() for b in [ball_bucket]*3]
        if result.count('R') >= result.count('G'):
            count += 1
    return count / num_trials


# print('Frequency of more reds than greends',
#       str(more_reds(100000) * 100) + '%')

def samecolor_dontreplace(num_trials):
    """
    simulate probability of rolling an even number
    :param num_trials: 
    :return: probability
    """
    count = 0
    for t in range(num_trials):
        result_list = []
        orig = ['G', 'G', 'G', 'R', 'R', 'R']
        for i in range(3):
            result_list.append(random.choice(orig))
            orig.remove(result_list[-1])
        if result_list == ['G','G','G'] or result_list == ['R','R','R']:
            count += 1
    return count / num_trials


print('Frequency of more reds than greends',
      str(samecolor_dontreplace(100000) * 100) + '%')

