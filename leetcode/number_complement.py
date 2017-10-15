# https://leetcode.com/problems/number-complement/

class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        bits = self.int2bin(num)
        for i in range(len(bits)):
            bits[i] = {0:1, 1:0}.get(bits[i])
        result = self.bin2int(bits)
        return result
        
        
    def int2bin(self, num):
        bits = []
        while num:
            bits.append(num % 2)
            num = num // 2
        return bits[::-1]
    def bin2int(self, bits):
        bits = bits[::-1]
        num = 0
        mult = 1
        for bit in bits:
            num += bit*mult
            mult = mult*2
        return num
