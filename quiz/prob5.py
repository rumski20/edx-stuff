# mid-term quiz | problem 5

def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """

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

    maxsum = 0
    for subset in get_all_subsets(L):
        if sum(subset) > maxsum:
            maxsum = sum(subset)

    return maxsum

# DEBUG
print('max contiguous sum:', max_contig_sum([5, -7, 1]))