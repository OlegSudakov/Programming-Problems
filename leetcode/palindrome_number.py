# https://leetcode.com/problems/palindrome-number/

import math

class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        if x < 10:
            return True
        l = int(math.floor(math.log10(x)))
        x1 = x
        while x:
            digit = x % 10
            x1 -= digit*10**l
            l -= 1
            x = x // 10
        if not x1:
            return True
        else:
            return False
