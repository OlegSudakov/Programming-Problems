# https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list

from copy import copy

"""
 Insert Node at a specific position in a linked list
 head input could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method. 
"""
#This is a "method-only" submission.
#You only need to complete this method.
def InsertNth(head, data, position):
    if head == None:
        head = Node(data)
        return head
    head_old = head
    if position == 0:
        return Node(data, head_old)
    for i in range(position - 1):
        if head.next == None:
            head.next = Node(data)
            return head_old
        head = head.next
    old_next = head.next
    head.next = Node(data)
    head.next.next = old_next
    return head_old
