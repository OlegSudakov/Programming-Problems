# https://leetcode.com/problems/most-frequent-subtree-sum/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        vals = []
        
        def __subtreeSum(root):
            if root is None:
                return 0
            else:
                curr_sum = __subtreeSum(root.left) + __subtreeSum(root.right) + root.val
                vals.append(curr_sum)
                return curr_sum
        
        __subtreeSum(root)
        counts = {}
        max_count = 0
        for val in vals:
            if val in counts:
                counts[val] += 1
            else:
                counts[val] = 1
            if counts[val] > max_count:
                max_count = counts[val]
        
        return [k for k, v in counts.items() if v == max_count]
