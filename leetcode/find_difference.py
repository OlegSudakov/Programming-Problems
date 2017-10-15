# https://leetcode.com/problems/find-the-difference/

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        counts = {}
        for char in s:
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
        
        for char in t:
            if char not in counts:
                return char
            else:
                counts[char] -= 1
                if counts[char] < 0:
                    return char
