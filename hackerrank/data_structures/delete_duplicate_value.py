# https://www.hackerrank.com/challenges/delete-duplicate-value-nodes-from-a-sorted-linked-list

"""
 Delete duplicate nodes
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def RemoveDuplicates(head):
    if head is None or head.next is None:
        return head
    current_elem = head
    next_elem = head.next
    while next_elem is not None:
        while next_elem.data == current_elem.data:
            next_elem = next_elem.next
            if next_elem is None:
                current_elem.next = None
                return head
        current_elem.next = next_elem
        current_elem = current_elem.next
        next_elem = next_elem.next
    return head
