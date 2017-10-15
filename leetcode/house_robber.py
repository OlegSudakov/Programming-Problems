# https://leetcode.com/problems/house-robber/

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.__rob(nums)[1]
    
    def __rob(self, nums):
        if not nums:
            return (0, 0)
        rest_robbed = self.__rob(nums[1:])
        return (rest_robbed[1], max(rest_robbed[0] + nums[0], rest_robbed[1]))
