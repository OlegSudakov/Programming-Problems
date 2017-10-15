# https://leetcode.com/problems/construct-the-rectangle/

import math

class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        root = int(math.sqrt(area))
        while area % root != 0:
            root -= 1
        return [area/root, root]
