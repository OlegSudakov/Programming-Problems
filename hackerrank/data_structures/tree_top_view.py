# https://www.hackerrank.com/challenges/tree-top-view

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)"""

def topView(root):
    elements = []
    curr_elem = root
    while curr_elem is not None:
        elements.append(str(curr_elem.data))
        curr_elem = curr_elem.left
    elements = elements[::-1]
    curr_elem = root.right
    while curr_elem is not None:
        elements.append(str(curr_elem.data))
        curr_elem = curr_elem.right
    print(" ".join(elements))
