# https://leetcode.com/problems/maximum-product-of-three-numbers/

class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        max_1 = nums[0]*nums[1]*nums[-1]
        max_2 = nums[0]*nums[-2]*nums[-1]
        max_3 = nums[-3]*nums[-2]*nums[-1]
        return max(max_1, max_2, max_3)
