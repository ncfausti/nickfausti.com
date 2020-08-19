class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""
        if n == 1:
            return s
        
        max_length = -1
        longest_substring = ""

        for i in range(n):
            #0:1, 0:2
            for j in range(i+1, n+1):
                if isPal(s[i:j]): # 0, 1
                    length = len(s[i:j])
                    if length > max_length:
                        max_length = length
                        longest_substring = s[i:j]
        return longest_substring
    
pals = set()

def isPal(s):
    N = len(s)
    if s in pals or N <= 1:
        return True
    if N == 2:
        if s[0] == s[1]:
            pals.add(s)
            return True
    
    if N % 2 == 0:
        # N == 12
        left = (N //2) - 1 # 5
        right = left + 1 # 6
        if s[left] != s[right]:
            return False
        current = s[left] + s[right]

        while len(current) < N:
            left -= 1
            right += 1

            if s[left] != s[right]:
                return False
            current = s[left] + current + s[right]
            pals.add(current)
    else:
        # N is odd, e.g. 5
        # 0 1 2 3 4
        # a b c b a
        mid = N // 2 # 2
        left = mid - 1 # 1
        right = mid + 1 # 3
        current = s[mid] # c

        while len(current) < N:
            if s[left] != s[right]:
                return False
            current = s[left] + current + s[right]
            pals.add(current)
            left -= 1
            right += 1

    return True
