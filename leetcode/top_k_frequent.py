# https://leetcode.com/problems/top-k-frequent-elements/

from collections import defaultdict

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts = {}
        max_count = 0
        
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
            if counts[num] > max_count:
                max_count = counts[num]
        
        counts_2 = defaultdict(list)
        for key, val in counts.items():
            counts_2[val].append(key)
        
        k_out = 0
        res = []
        for i in range(max_count, 0, -1):
            if i in counts_2:
                for elem in counts_2[i]:
                    res.append(elem)
                    k_out += 1
                    if k_out >= k:
                        return res
        return res
