# https://leetcode.com/problems/excel-sheet-column-number/

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        sum = 0
        mult = 1
        s = s[::-1]
        for char in s:
            sum += mult*(ord(char) - ord('A') + 1)
            mult *= 26
        return sum
