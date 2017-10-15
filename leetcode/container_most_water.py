# https://leetcode.com/problems/container-with-most-water/

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start = 0
        end = len(height) - 1
        distance = end - start
        max_w = distance*min(height[start], height[end])
        while start < end:
            if height[start] <= height[end]:
                start += 1
            elif height[start] > height[end]:
                end -= 1
            distance = end - start
            if distance*min(height[start], height[end]) > max_w:
                max_w = distance*min(height[start], height[end])
        return max_w
