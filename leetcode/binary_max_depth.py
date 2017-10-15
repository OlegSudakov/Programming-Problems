# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.__maxDepth(root, 0)
    
    def __maxDepth(self, root, d):
        if root is None:
            return d
        else:
            return max(self.__maxDepth(root.left, d+1), self.__maxDepth(root.right, d+1))
