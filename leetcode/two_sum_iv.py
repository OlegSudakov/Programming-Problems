# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        bfs, s = [root], set()
        while bfs:
            current = bfs.pop()
            if k - current.val in s:
                return True
            s.add(current.val)
            if current.left:
                bfs.append(current.left)
            if current.right:
                bfs.append(current.right)
        return False
