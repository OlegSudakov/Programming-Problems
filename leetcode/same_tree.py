# https://leetcode.com/problems/same-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        return self.__isSameTree(p, q)
        
    def __isSameTree(self, p, q):
        if p is None and q is None:
            return True
        if p is None and q is not None:
            return False
        if q is None and p is not None:
            return False
        return self.__isSameTree(p.left, q.left) and p.val == q.val and self.__isSameTree(p.right, q.right)
        
