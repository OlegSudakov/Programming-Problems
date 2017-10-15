# https://www.hackerrank.com/challenges/tree-level-order-traversal

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
import sys

def levelOrder(root):
    queue = []
    queue.append(root)
    while queue:
        root = queue.pop(0)
        sys.stdout.write("{} ".format(root.data))
        if root.left is not None:
            queue.append(root.left)
        if root.right is not None:
            queue.append(root.right)
