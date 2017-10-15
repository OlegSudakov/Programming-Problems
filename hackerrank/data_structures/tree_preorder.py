# https://www.hackerrank.com/challenges/tree-preorder-traversal

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""

import sys


def preOrder(root):
    vals = []
    if root is not None:
        sys.stdout.write(str(root.data)+" ")
        preOrder(root.left)
        preOrder(root.right)
