# https://leetcode.com/problems/add-digits/

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num < 10:
            return num
        else:
            sum = 0
            while num:
                sum += num % 10
                num /= 10
            return self.addDigits(sum)
