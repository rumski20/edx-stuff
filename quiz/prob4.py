# mid-term quiz | problem 3

def greedySum(L, s):
    """ input: s, positive integer, what the sum should add up to
               L, list of unique positive integers sorted in descending order
        Use the greedy approach where you find the largest multiplier for 
        the largest value in L then for the second largest, and so on to 
        solve the equation s = L[0]*m_0 + L[1]*m_1 + ... + L[n-1]*m_(n-1)
        return: the sum of the multipliers or "no solution" if greedy approach does 
                not yield a set of multipliers such that the equation sums to 's'
    """


    # find largest multiplier that doesn't exceed a value
    def find_largest_multiplier(n, sub):
        m = 0
        while n * m <= sub:
            m += 1
        # use minus one since it increments before it can get returned
        return m-1

    # multiplier list
    m_list = []
    # remaining minimum
    remaining = s

    # loop through list of integers
    for x in range(len(L)):
        # find largest multiple for int in list
        m = find_largest_multiplier(L[x], remaining)
        m_list.append(m)
        # subtract from remaining
        remaining -= L[x] * m

    # check for empty list
    if not m_list or remaining != 0:
        return "no solution"

    # return sum of multipliers
    return sum(m_list)
    # return m_list

# DEBUG
print("=====================")
listy = [10,7,6,3]
sumy = 19
print("Multipliers {0} for {1} equals {2}".format(greedySum(listy, sumy),
                                                  listy, sumy))
