# https://leetcode.com/problems/average-of-levels-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        avgs = [root.val]
        
        nodes = [root]
        new_nodes = []
        for leaf in nodes:
            if leaf.right is not None:
                new_nodes.append(leaf.right)
            if leaf.left is not None:
                new_nodes.append(leaf.left)
        
        while new_nodes:
            nodes = new_nodes
            avgs.append(1.0*sum([leaf.val for leaf in nodes])/len(nodes))
            new_nodes = []
            for leaf in nodes:
                if leaf.right is not None:
                    new_nodes.append(leaf.right)
                if leaf.left is not None:
                    new_nodes.append(leaf.left)
        return avgs
