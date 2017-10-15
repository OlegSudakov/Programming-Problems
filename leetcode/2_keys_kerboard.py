# https://leetcode.com/problems/2-keys-keyboard/

import math

class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        operations = 0
        target = n
        if target == 1:
            return operations
        while target:
            prime_flag = True
            for i in range(2, int(math.floor(target / 2))):
                if target % i == 0:
                    prime_flag = False
                    operations += 1+(i-1)
                    target = target / i
                    break
            if prime_flag:
                operations += target
                target = 0
        return operations
