# https://leetcode.com/problems/array-partition-i/

class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        nums.sort()
        for i in range(1, len(nums), 2):
            result += min(nums[i], nums[i-1])
        return result
