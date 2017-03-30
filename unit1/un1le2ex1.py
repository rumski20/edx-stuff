# Unit 1 | Lecture 2 | Exercise 1

from ref import items


# example
# generate all combinations of N items
def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2 ** N):
        combo = []
        for j in range(N):
            print(i, str(bin(i))[2:], j)
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        print('combo: ', combo)
        yield combo

test_list = items.buildRandomItems(3)
# test_list = [1,2,3,4]
print('power set - one bag', test_list)
print(len([i for i in powerSet(test_list)]), 'combinations')

# jiPiBi's power set method
def powerSet2(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2 ** N):
        combo = []
        n = i
        for j in range(N):
            print(i, j, n)
            if n % 2 == 1:
                combo.append(items[j])
            n //= 2
        print('combo: ', combo)
        yield (combo)


# test_list = [1, 2, 3]
# print('power set - one bag', test_list)
# print(len([i for i in powerSet2(test_list)]), 'combinations')


def yieldAllCombos(items):
    """
      Generates all combinations of N items into two bags, whereby each
      item is in one or zero bags.

      Yields a tuple, (bag1, bag2), where each bag is represented as
      a list of which item(s) are in each bag.
    """
    # for item1 in items:
    #     for item2 in items:
    #         bag1 = []
    #         bag2 = []
    #         if item1 not in bag1:
    #             bag1.append(item1)

    N = len(items)
    runninglist = []
    # enumerate the 3**N possible combinations
    # for a in range(2 ** N):
    #     for b in range(2 ** N):
    #         bag1 = []
    #         bag2 = []
    #         for c in range(N):
    #             print(a, str(bin(a))[2:], b, (b >> c), c)
    #             if (a >> c) % 2 == 1:
    #                 bag1.append(items[c].getName())
    #             if (b >> c) % 3 == 2:
    #                 bag2.append(items[c].getName())
    #     print('combo: ', (bag1, bag2))
    #     yield (bag1, bag2)

    for a in range(2 ** N):
        for b in range(2 ** N):
            bag1 = []
            bag2 = []
            for c in range(N):
                d = ((a >> c) % 2) + ((b >> c) % 2)
                # print(a,b,c,d)
                if d == 1:
                    bag1.append(items[c].getName())
                if d == 2:
                    bag2.append(items[c].getName())
            if (bag1,bag2) not in runninglist:
                # print('combo: ', (bag1, bag2))
                yield (bag1, bag2)
            runninglist.append((bag1,bag2))
            # print(runninglist, (bag1,bag2))


# print('power set - two bag')
# # test_list = items.buildRandomItems(3)
# test_list = items.buildItems()
# [print(i) for i in test_list]
# print(len([i for i in yieldAllCombos(test_list)]), 'combinations')
