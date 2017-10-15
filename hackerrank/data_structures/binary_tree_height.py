# https://www.hackerrank.com/challenges/tree-height-of-a-binary-tree

'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''
def height_rec(root, h):
    if root is None:
        return h-1
    else:
        return max(height_rec(root.left, h+1), height_rec(root.right, h+1))

def height(root):
    return height_rec(root, 0)
