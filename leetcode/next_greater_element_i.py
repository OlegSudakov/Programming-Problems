# https://leetcode.com/problems/next-greater-element-i/

class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        nums_inds = {}
        for i in range(len(nums)):
            nums_inds[nums[i]] = i
        
        result = []
        for num in findNums:
            if num not in nums:
                result.append(-1)
            else:
                pos = nums_inds[num]
                found_num = False
                for num_2 in nums[pos+1:]:
                    if num_2 > num:
                        result.append(num_2)
                        found_num = True
                        break
                if not found_num:
                    result.append(-1)
        return result
