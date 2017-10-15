# https://leetcode.com/problems/binary-tree-right-side-view/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        right_nodes = [root.val]
        nodes = [root]
        new_nodes = []
        for leaf in nodes:
            if leaf.left is not None:
                new_nodes.append(leaf.left)
            if leaf.right is not None:
                new_nodes.append(leaf.right)
                
        while new_nodes:
            nodes = new_nodes
            right_nodes.append(nodes[-1].val)
            new_nodes = []
            for leaf in nodes:
                if leaf.left is not None:
                    new_nodes.append(leaf.left)
                if leaf.right is not None:
                    new_nodes.append(leaf.right)
        return right_nodes
