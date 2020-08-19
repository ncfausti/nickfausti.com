import heapq
from collections import deque
from itertools import product, combinations, combinations_with_replacement, permutations

# Use heapq to efficientl keep track of updated values from list
from heapq import merge


def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    results = list(merge(nums1, nums2))
    N = len(results)
    if N % 2 == 0:
        mid = (N // 2) - 1 # 12 -> 6-1 = 5
        # mid + 2 since python list slice 0:2 returns 0, 1 elements
        return sum(results[mid:mid+2]) / 2 
    return results[N//2] # e.g. 5 -> 2 0,1, 2 ,3 4
        
        



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


