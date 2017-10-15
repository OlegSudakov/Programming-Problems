# https://leetcode.com/problems/binary-tree-postorder-traversal/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.list = []
        
    def postorderTraversal(self, root):
        self.__postorderTraversal(root)
        return self.list
        
    def __postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return
        self.__postorderTraversal(root.left)
        self.__postorderTraversal(root.right)
        self.list.append(root.val)
