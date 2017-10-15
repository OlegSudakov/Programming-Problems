# https://www.hackerrank.com/challenges/binary-search-tree-lowest-common-ancestor

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
def lca(root , v1 , v2):
    if root is None:
        return None
    while root is not None:
        if v1 > root.data and v2 > root.data:
            root = root.right
        elif v1 < root.data and v2 < root.data:
            root = root.left
        else:
            return root
