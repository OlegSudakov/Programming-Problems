# https://leetcode.com/problems/sort-characters-by-frequency/

from collections import defaultdict

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        counts = {}
        max_chars = 0
        
        for char in s:
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
            if counts[char] > max_chars:
                max_chars = counts[char]
                
        res = ""
        chars = defaultdict(list)
        for k, v in counts.items():
            chars[v].append(k)
        
        for i in range(max_chars, 0, -1):
            if i in chars:
                for char in chars[i]:
                    res += char*i
        return res
