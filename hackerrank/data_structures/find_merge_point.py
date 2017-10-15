# https://www.hackerrank.com/challenges/find-the-merge-point-of-two-joined-linked-lists

"""
 Find the node at which both lists merge and return the data of that node.
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 
"""

def FindMergeNode(headA, headB):
    lenA, lenB = 0, 0
    elemA = headA; elemB = headB
    while elemA is not None:
        elemA = elemA.next
        lenA += 1
    while elemB is not None:
        elemB = elemB.next
        lenB += 1
    elemA = headA; elemB = headB
    if lenA > lenB:
        for i in range(lenA - lenB):
            elemA = elemA.next
    elif lenB > lenA:
        for i in range(lenB - lenA):
            elemB = elemB.next
    while elemA is not None:
        if elemA.data == elemB.data:
            return elemA.data
        elemA = elemA.next
        elemB = elemB.next
