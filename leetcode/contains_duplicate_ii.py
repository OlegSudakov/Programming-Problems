# https://leetcode.com/problems/contains-duplicate-ii/

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        last_indice = {}
        for i in range(len(nums)):
            if nums[i] in last_indice:
                if abs(i - last_indice[nums[i]]) <= k:
                    return True
            last_indice[nums[i]] = i
        return False
        
