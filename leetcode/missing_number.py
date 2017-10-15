# https://leetcode.com/problems/missing-number/

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n_visited = False
        for n in nums:
            if n < 0:
                index = -(n + 1)
            else:
                index = n
            if index == len(nums):
                n_visited = True
            else:
                nums[index] = -nums[index]-1
        if not n_visited:
            return len(nums)
        else:
            for i in range(len(nums)):
                if nums[i] >= 0:
                    return i
