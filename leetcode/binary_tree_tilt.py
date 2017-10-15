# https://leetcode.com/problems/binary-tree-tilt/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.__findTilt(root)[1]
    
    def __findTilt(self, root):
        if root is None:
            return 0, 0
        
        else:
            sum_left, tilt_sum_left = self.__findTilt(root.left)
            sum_right, tilt_sum_right = self.__findTilt(root.right)
            tilt = abs(sum_left - sum_right)
            return sum_left + root.val + sum_right, tilt_sum_left + tilt + tilt_sum_right
