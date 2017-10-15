# https://leetcode.com/problems/path-sum/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def __init__(self):
        self.paths = []
        
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.__pathSum(root, sum, [], 0)
        return self.paths
    
    


class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        return self.__pathSum(root, sum, [], 0)
        
    def __pathSum(self, root, sum, path, prev_sum):
        if root is None:
            return False
        elif root.left is None and root.right is None:
            if prev_sum + root.val == sum:
                return True
            else:
                return False
        else:
            return self.__pathSum(root.left, sum, path + [root.val], prev_sum + root.val) or \
                self.__pathSum(root.right, sum, path + [root.val], prev_sum + root.val)
