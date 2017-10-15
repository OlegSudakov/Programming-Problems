# https://leetcode.com/problems/power-of-two/

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        if n % 2 == 0:
            if n:
                return self.isPowerOfTwo(n // 2)
            else:
                return False
        else:
            return False
