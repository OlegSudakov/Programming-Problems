# https://www.hackerrank.com/challenges/merge-two-sorted-linked-lists

"""
 Merge two linked lists
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def MergeLists(headA, headB):
    new_head = None
    if headA is None:
        return headB
    if headB is None:
        return headA
    if headA is not None and headB is not None:
        if headA.data < headB.data:
            new_head = headA
            headA = headA.next
        else:
            new_head = headB
            headB = headB.next
    current_elem = new_head
    while headA is not None and headB is not None:
        if headA.data < headB.data:
            current_elem.next = headA
            headA = headA.next
        else:
            current_elem.next = headB
            headB = headB.next
        current_elem = current_elem.next
    if headA is None:
        current_elem.next = headB
    if headB is None:
        current_elem.next = headA
    return new_head
