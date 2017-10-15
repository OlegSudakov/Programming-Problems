# https://leetcode.com/problems/path-sum-iii/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.paths = 0
        
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.__pathSum(root, sum, [])
        return self.paths
        
        
    def __pathSum(self, root, sum, prev_sums):
        if root is None:
            return
        else:
            prev_sums = [prev_sum + root.val for prev_sum in prev_sums] + [root.val]
            for i in range(len(prev_sums)):
                if prev_sums[i] == sum:
                    self.paths += 1
            self.__pathSum(root.left, sum, prev_sums)
            self.__pathSum(root.right, sum, prev_sums)
