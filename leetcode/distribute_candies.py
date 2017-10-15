# https://leetcode.com/problems/distribute-candies/

class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        counts = {}
        for candy in candies:
            if candy in counts:
                counts[candy] += 1
            else:
                counts[candy] = 1
        return min(len(candies)//2, len(counts))
