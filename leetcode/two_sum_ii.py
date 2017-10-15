# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        indices = {}
        for i in range(len(numbers)):
            if target - numbers[i] in indices:
                return [indices[target - numbers[i]]+1, i+1]
            else:
                indices[numbers[i]] = i
        return None
