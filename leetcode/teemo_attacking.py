# https://leetcode.com/problems/teemo-attacking/

class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if len(timeSeries) == 0:
            return 0
        total = 0
        start = timeSeries[0]
        end = start + duration - 1
        
        for t in timeSeries[1:]:
            if t > end:
                total += end - start + 1
                start = t
                end = start + duration - 1
            else:
                end = t + duration - 1
        total += end - start + 1
        return total
