# https://www.hackerrank.com/challenges/is-binary-search-tree

""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
def check_binary_search_tree(root):
    if root is None:
        return True, None, None # BST flag, min, max
    
    if root.left is None and root.right is None:
        return True, root.data, root.data
    
    elif root.left is not None and root.right is None:
        flag, min_val, max_val = check_binary_search_tree(root.left)
        if flag and max_val < root.data:
            return True, min_val, root.data
        else:
            return False, min_val, max_val
        
    elif root.right is not None and root.left is None:
        flag, min_val, max_val = check_binary_search_tree(root.right)
        if flag and root.data < min_val:
            return True, root.data, max_val
        else:
            return False, min_val, max_val
        
    else:
        flag_left, min_val_left, max_val_left = check_binary_search_tree(root.left)
        flag_right, min_val_right, max_val_right = check_binary_search_tree(root.right)
        if flag_left and flag_right and max_val_left < root.data < min_val_right:
            return True, min_val_left, max_val_right
        else:
            return False, root.data, root.data
    
            
def check_binary_search_tree_(root):
    flag, _, _  = check_binary_search_tree(root)
    return flag
