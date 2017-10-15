# https://leetcode.com/problems/construct-string-from-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if t is None:
            return ""
        if t.left is None and t.right is None:
            return str(t.val)
        elif t.right is None:
            return "{}({})".format(t.val, self.tree2str(t.left))
        elif t.left is None:
            return "{}()({})".format(t.val, self.tree2str(t.right))
        else:
            return "{}({})({})".format(t.val, self.tree2str(t.left), self.tree2str(t.right))
