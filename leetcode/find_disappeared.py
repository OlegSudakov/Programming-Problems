# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = -abs(nums[index])
        return [n+1 for n in range(len(nums)) if nums[n] > 0]
