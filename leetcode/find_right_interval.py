# https://leetcode.com/problems/find-right-interval/

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
from collections import defaultdict

class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        start = {}
        max_start = -1
        for i in range(len(intervals)):
            if intervals[i].start not in start:
                start[intervals[i].start] = i
            if intervals[i].start > max_start:
                max_start = intervals[i].start
        res = [-1] * len(intervals)
        for i in range(len(intervals)):
            if intervals[i].end in start:
                res[i] = start[intervals[i].end]
            else:
                for j in range(intervals[i].end, max_start + 1):
                    if j in start:
                        res[i] = start[j]
                        break
        return res
