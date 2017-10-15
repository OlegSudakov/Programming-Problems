# https://leetcode.com/problems/remove-element/

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        pos = 0
        count = 0
        
        for i in range(len(nums)):
            if nums[i] == val:
                count += 1
            else:
                nums[pos] = nums[i]
                pos += 1
        return len(nums) - count
