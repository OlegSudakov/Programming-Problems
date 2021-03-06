# https://www.hackerrank.com/challenges/reverse-a-linked-list

"""
 Reverse a linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def Reverse(head):
    new_head = None
    while head != None:
        new_head = Node(head.data, next_node = new_head)
        head = head.next
    return new_head
