# https://www.hackerrank.com/challenges/tree-postorder-traversal

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
import sys

def postOrder(root):
    vals = []
    if root is not None:
        postOrder(root.left)
        postOrder(root.right)
        sys.stdout.write(str(root.data)+" ")
