def increasingTriplet(nums: List[int]) -> bool:
    N = len(nums)
    if N < 2:
        return False
    
    # 10 0 5 3 19 2 25
    for i in range(0, N-1):
        # if the number following this one is less, that should be 
        # the starting number.
        if nums[i] < nums[i+1]:

            # next number is now greater than current number
            # only need to find one more num greater than mid, bc mid will
            # already be greater than list[index_of_mid-1]
            # at each check for j, see if we can get a lower mid that is still higher
            # than start, this will "increase the slack" we have for finding a nums[j] 
            # greater than both start AND mid.
            
            start = nums[i] # 3
            mid = nums[i+1] # 4 
            
            for j in range(i+2, N): # 5 3 4 5
                if nums[j] < mid and nums[j] > start:
                    mid = nums[j]
                if nums[j] > mid > start:
                    
                    return True
    return False
    
# post-mortem: 
#    names matter! poorly named variables will confuse me
#    solve problems on paper first
#    check my assumptions
#    be extremely detail-oriented and keep track of each line of code
#    believe in myself :)
#    stop comparing myself to others

        
# heuristics noticed:
#   lowest number and to the left are best  for starting values

assert increasingTriplet([1, 3, 1, 3, -3, 9, 2]) == True
assert increasingTriplet([5,1,5,5,2,5,4]) == True
assert increasingTriplet([5,4,3,2,1]) == False

    