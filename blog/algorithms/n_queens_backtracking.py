"""
Given: N x N board:
- - -
- - -
- - -
0 1 2

Output: The permuation that satisfies the N-queens problem.

Is the current permutation of queen placements
(represented by the indices below the board) a 
solution.

is_solution([1,3,0,2])
e.g.

- Q - -
- - - Q 
Q - - - 
- - Q - 
1 3 0 2

Return True

This works because no two queens are on the same diagonal.
"""

# Key Observation, to tell if on same diagonal, check
# if index1
def is_solution(perm):
    for (i1, i2) in combinations(range(len(perm)), 2):
        # If on same diagonal i.e. 45 degree line, return false
        if abs(i1 - i2) == abs(perm[i1] - perm[i2]):
            return False
    
    return True


# Iterate through all permutations of (012...7)
for perm in permutations(range(8)):
    if is_solution(perm):
        print(perm)
        exit()
