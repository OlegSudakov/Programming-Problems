# https://leetcode.com/problems/4sum-ii/

class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        counts = {}
        for a in A:
            for b in B:
                if a+b in counts:
                    counts[a+b] += 1
                else:
                    counts[a+b] = 1
        total = 0
        for c in C:
            for d in D:
                if -c-d in counts:
                    total += counts[-c-d]
        return total
        
