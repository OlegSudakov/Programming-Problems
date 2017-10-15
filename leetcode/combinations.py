# https://leetcode.com/problems/combinations/

class Solution(object):
    def __init__(self):
        self.res = []
    
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self._combine(k, list(range(1, n+1)), [])
        return self.res
        
    
    def _combine(self, k, nums, picked):
        if len(picked) == k:
            self.res.append(picked)
            return
        if not nums:
            return
        for i in range(len(nums) - (k - len(picked))+1):
            self._combine(k, nums[i+1:], picked+[nums[i]])
