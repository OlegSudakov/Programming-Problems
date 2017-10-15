# https://www.hackerrank.com/challenges/get-the-value-of-the-node-at-a-specific-position-from-the-tail

"""
 Get Node data of the Nth Node from the end.
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the node data of the linked list in the below method.
""" 

def GetNode(head, position):
    old_head = head
    length = 0
    while head is not None:
        head = head.next
        length += 1
    head = old_head
    steps_taken = 0
    while length - steps_taken - 1 != position:
        head = head.next
        steps_taken += 1
    return head.data
