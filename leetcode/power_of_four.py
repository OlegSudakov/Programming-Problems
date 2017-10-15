# https://leetcode.com/problems/power-of-four/

import math

class Solution(object):
    def isPowerOfFour(self, num):
        if num <= 0:
            return False
        log = math.log(num, 4)
        if math.ceil(log) == math.floor(log):
            return True
        else:
            return False
