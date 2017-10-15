# https://leetcode.com/problems/count-numbers-with-unique-digits/

class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        sum = 10
        mult = 9
        res = mult
        for i in range(1, n):
            res = res*mult
            sum += res
            mult -= 1
            if mult < 1:
                break
        return sum
