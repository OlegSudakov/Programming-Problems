# https://leetcode.com/problems/binary-tree-paths/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __binaryTreePaths(self, root, string):
        if root is None:
            return []
        if string:
            new_string = string+"->{}".format(root.val)
        else:
            new_string = str(root.val)
        if root.left is None and root.right is None:
            return [new_string]
        return self.__binaryTreePaths(root.left, new_string) + self.__binaryTreePaths(root.right, new_string)
    
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root is None:
            return []
        return self.__binaryTreePaths(root, "")
