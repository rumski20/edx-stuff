# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 14:33:33 2017

@author: kristofj
"""

# 1.
NUMBER = 3
def look_for_things(myList):
    """Looks at all elements"""
    for n in myList:
        print(n)
        if n == NUMBER:
            return True
    return False

print("Look for things:", "\n", look_for_things([1,2,3,4,5,6]), "\n")

# 2.
NUMBER = 3
def look_for_other_things(myList):
    """Looks at all pairs of elements"""
    for n in myList:
        for m in myList:
            print(n,m)
            if n - m == NUMBER or m - n == NUMBER:
                return True
    return False

print("Look for other things:", "\n", look_for_other_things([1,2,3,4,5,6]), "\n")

# 3.
def get_all_subsets(some_list):
    """Returns all subsets of size 0 - len(some_list) for some_list"""
    if len(some_list) == 0:
        # If the list is empty, return the empty list
        return [[]]
    subsets = []
    first_elt = some_list[0]
    rest_list = some_list[1:]
    # Strategy: Get all the subsets of rest_list; for each
    # of those subsets, a full subset list will contain both
    # the original subset as well as a version of the subset
    # that contains first_elt
    for partial_subset in get_all_subsets(rest_list):
        subsets.append(partial_subset)
        next_subset = partial_subset[:] + [first_elt]
        subsets.append(next_subset)
    return subsets

NUMBER = 3
def look_for_all_the_things(myList):
    """Looks at all subsets of this list"""
    # Make subsets
    all_subsets = get_all_subsets(myList)
    print(all_subsets)
    for subset in all_subsets:
        print(subset)
        if sum(subset) == NUMBER:
            return True
    return False

print("Look for all the things:", "\n", look_for_all_the_things([1,2,3]), "\n")