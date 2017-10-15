# https://leetcode.com/problems/house-robber-iii/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.__rob(root)[1]
        
    def __rob(self, root):
        if root is None:
            return (0,0)
        l = self.__rob(root.left)
        r = self.__rob(root.right)
        return (l[1] + r[1], max(l[1] + r[1], l[0] + r[0] + root.val))
        
