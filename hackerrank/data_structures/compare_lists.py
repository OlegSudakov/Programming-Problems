# https://www.hackerrank.com/challenges/compare-two-linked-lists

"""
 Merge two linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def CompareLists(headA, headB):
    while (headA is not None) or (headB is not None):
        if ((headA is None) != (headB is None)) or (headA.data != headB.data):
            return 0
        headA = headA.next
        headB = headB.next
    return 1
