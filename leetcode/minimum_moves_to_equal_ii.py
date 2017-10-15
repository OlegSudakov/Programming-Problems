# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/

import math

class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        median = sorted(nums)[len(nums)/2]
        return sum([abs(median - num) for num in nums])
