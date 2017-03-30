###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time


# ================================
# Part A: Transporting Space Cows
# ================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')

    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows, limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # key function for sorting cows
    key_func = lambda x: x[1]
    # get sorted copy of cows dictionary based on key function
    # and since we can't sort hash tables (dicts) so this is an
    # ordered list of (key, val) tuples
    cows_copy = sorted(cows.items(), key=key_func, reverse=True)
    print('cows copy', cows_copy)
    result = []

    # while there are still cows to be transported
    while cows_copy:
        totcost = 0
        shiplist = []
        # create a copy of a copy
        cows_copy_copy = cows_copy[:]
        # loop through cows
        for cow in cows_copy_copy:
            # check if cow will tip scales
            if (totcost + cow[1]) <= limit:
                shiplist.append(cow[0])
                totcost += cow[1]
                cows_copy.remove(cow)

        # add shiplist to result
        result.append(shiplist)

    return result


# Problem 2
def brute_force_cow_transport(cows, limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # copy input dict in list of tuple pairs
    # ref: http://stackoverflow.com/a/22214248/6072959
    cows_copy = [(k, v) for k, v in cows.items()]
    shiplist = []

    # get all the partitions
    cow_parts = get_partitions(cows_copy)
    # loop through partitions
    for part in cow_parts:
        # loop through combos in partition
        for combo in part:
            # check if cow will tip scales
            combotot = sum([c[1] for c in combo])
            if combotot > limit:
                break
        # if no combo tips the scales add partition and it's length to list
        # get just cow names
        else:
            cowname_list = [[c[0] for c in combo] for combo in part]
            shiplist.append((cowname_list, len(cowname_list)))

    # key function for sorting cows
    key_func = lambda x: x[1]
    # return partition list with fewest trips
    result = sorted(shiplist, key=key_func)[0][0]
    return result


# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    cows = load_cows("ps1_cow_data.txt")
    limit = 10
    print(cows)

    # greedy
    greedy_start = time.time()
    greedy_count = len(greedy_cow_transport(cows, limit))
    greedy_end = time.time()
    print('greedy:', '{0} trips in {1}s'.format(greedy_count,
                                                greedy_end - greedy_start))

    # brute_force
    brute_force_start = time.time()
    brute_force_count = len(brute_force_cow_transport(cows, limit))
    brute_force_end = time.time()
    print('brute_force:', '{0} trips in {1}s'
          .format(brute_force_count, brute_force_end - brute_force_start))


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

# cows = load_cows("ps1_cow_data.txt")
# cows = {'Lotus': 10, 'Clover': 5, 'Miss Bella': 15,
#         'MooMoo': 85, 'Milkshake': 75, 'Patches': 60,
#         'Polaris': 20, 'Horns': 50, 'Muscles': 65, 'Louis': 45}
# limit=10
# print(cows)

# print('greedy:', greedy_cow_transport(cows, limit))
# print('greedy test1:', greedy_cow_transport(cows, 100))
# print('brute:', brute_force_cow_transport(cows, 100))
print('comparision:', compare_cow_transport_algorithms())
