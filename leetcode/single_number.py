# https://leetcode.com/problems/single-number/

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1, len(nums)):
            nums[i] = nums[i] ^ nums[i-1]
        return nums[-1]
