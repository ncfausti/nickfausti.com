"""
Given a sorted array, return the index of the number. 
If not found return -1.
"""

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2

        if x > arr[mid]:
            low = mid + 1
        elif x < arr[mid]:
            # move end to mid 
            high = mid - 1
        else:
            return mid

    return -1

    # find the middle element
    # check if item is > or < then
    # update start, end
    # repeat

arr1 = [1,2,3,4,5,6,7,8,9]
arr2 = [1,3,4,55,66,322,999,90999]

assert binary_search(arr1, 4) == 3
assert binary_search(arr2, 66) == 4
assert binary_search(arr1, 1) == 0
assert binary_search(arr1, 5) == 4
assert binary_search(arr1, -3) == -1
assert binary_search(arr1, 9999) == -1



