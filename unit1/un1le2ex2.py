# unit 1 | lecture 2 | exercise 2
# powersets using itertools library

from itertools import chain, combinations
from ref import items


def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


# for result in powerset([1, 2, 3]):
#     print(result)
#
# results = list(powerset([1, 2, 3]))
# print(results)

print('power set - itertools')
test_list = items.buildRandomItems(3)
# test_list = items.buildItems()
[print(i) for i in test_list]
print(len([i for i in powerset(test_list)]), 'combinations:', \
      [print(result) for result in powerset(test_list)])
