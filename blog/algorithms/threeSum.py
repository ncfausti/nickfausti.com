class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # generate all possible twoSums and store sum_value-> [ [val1, val2, i, j], ... ]
        # iterate over list once more to check if (0 - number) in dictionary

        # sum_value-> [ [val1, val2, i, j], ... ]
        pairs = dict()
        matches = []
        N = len(nums)

        # generate all pairs, O(n choose 2)
        for i in range(N):
            for j in range(i+1, N):
                pairsum = nums[i] + nums[j]
                if pairsum in pairs:
                    pairs[pairsum].append([nums[i], nums[j], i, j])
                else:
                    pairs[pairsum] = [[nums[i], nums[j], i, j]]

        # check if diff in dictionary keys, if so, make sure not reusing current index
        for i in range(N):
            diff = 0 - nums[i]
            if diff in pairs:
                # pairs[diff]: [][]
                # p: [val1, val2, idx1, idx2]
                for p in pairs[diff]:
                    if i != p[2] and i != p[3]:
                        match = sorted([nums[i], p[0], p[1]])
                        if not match in matches:
                            matches.append(match)

        return matches
