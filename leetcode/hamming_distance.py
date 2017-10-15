# https://leetcode.com/problems/hamming-distance/

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        xor = x ^ y
        return sum(self.int2bin(xor))
        
    def int2bin(self, num):
        bits = []
        while num:
            bits.append(num % 2)
            num = num // 2
        bits = bits[::-1]
        return bits
