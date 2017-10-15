# https://www.hackerrank.com/challenges/binary-search-tree-insertion

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)"""

def insert(r,val):
    if r is None:
        r = Node(val)
        return r
    curr_root = r
    while True:
        if val > curr_root.data:
            if curr_root.right is None:
                curr_root.right = Node(val)
                return r
            else:
                curr_root = curr_root.right
        else:
            if curr_root.left is None:
                curr_root.left = Node(val)
                return r
            else:
                curr_root = curr_root.left
