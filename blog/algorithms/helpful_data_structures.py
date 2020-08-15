import heapq
from collections import deque
from itertools import product, combinations, combinations_with_replacement, permutations

# product(ls, repeat=2)
# https://docs.python.org/3.8/library/itertools.html


def all_perms(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                # nb elements[0:1] works in both string and list contexts
                yield perm[:i] + elements[0:1] + perm[i:]


