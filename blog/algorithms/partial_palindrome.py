"""
Given a number n, return if it is 1-off 
from being a palindrome. If it is not, 1
number away from being a palindrome, print
which numbers are off.

Test Cases:
123321 -> False # is a palindrome
99598  -> True, # prints 9, 8 
753772 -> False # is more than 1 off

Method:

use n % 10 to get last digit
use n // 10 to remove last digit
build reversed number, at each point check to see if 
reversed is equal to n at location, if not update offby

if offby == 1 return true and print diff
else return false
"""
import math

def partial_palindrome(n):
    s = str(n)
    offby = 0
    while (len(s) > 0):
        if s[0] != s[-1]:
            print(s[0], s[-1])
            if offby == 1:
                return False
            offby += 1
        s = s[1:-1]
    print(offby == 1)
    return offby == 1

partial_palindrome(12322)

        



