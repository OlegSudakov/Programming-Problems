# https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.list = []
        
    def inorderTraversal(self, root):
        self.__inorderTraversal(root)
        return self.list
        
    def __inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root:
            self.inorderTraversal(root.left)
            self.list.append(root.val)
            self.inorderTraversal(root.right)
