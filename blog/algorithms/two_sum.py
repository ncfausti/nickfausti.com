from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    seen = dict()
    for i, num in enumerate(nums):
        strDiff = str(target - num)
        if strDiff in seen:
            return [seen[strDiff], i]
        else:
            seen[str(num)] = i
    return []


assert two_sum([9, 2, 7, 13, 10,11], 9) == [1, 2]
assert two_sum([9, 2, 7, 13, 10,11], 99) == []
assert two_sum([], 9) == []
