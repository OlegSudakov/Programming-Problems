# https://leetcode.com/problems/valid-anagram/

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        counts_s = {}; counts_t = {}
        for char in s:
            if char in counts_s:
                counts_s[char] += 1
            else:
                counts_s[char] = 1
        for char in t:
            if char in counts_t:
                counts_t[char] += 1
            else:
                counts_t[char] = 1
        for char in counts_s:
            if char not in counts_t or counts_s[char] != counts_t[char]:
                return False
        for char in counts_t:
            if char not in counts_s:
                return False
        return True
