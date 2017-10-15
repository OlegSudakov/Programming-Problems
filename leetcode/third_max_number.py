# https://leetcode.com/problems/third-maximum-number/

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)[::-1]
        unique_seen = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                unique_seen += 1
            if unique_seen == 3:
                return nums[i]
        return nums[0]
