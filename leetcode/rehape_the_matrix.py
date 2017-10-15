# https://leetcode.com/problems/reshape-the-matrix/

class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if r*c != len(nums)*len(nums[0]):
            return nums
        
        new_matrix = []
        for i in range(r):
            new_matrix.append([0]*c)
        x, y = 0, 0
        for i in range(len(nums)):
            for j in range(len(nums[0])):
                new_matrix[y][x] = nums[i][j]
                x += 1
                if x == c:
                    x = 0
                    y += 1
        return new_matrix
