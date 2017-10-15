# https://leetcode.com/problems/isomorphic-strings/

class Solution(object):
    def computePattern(self, word):
        index = 0
        seen = {}
        pattern = []
        for char in word:
            if char in seen:
                pattern.append(seen[char])
            else:
                seen[char] = index
                pattern.append(seen[char])
                index += 1
        return pattern
                
    
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return self.computePattern(s) == self.computePattern(t)
