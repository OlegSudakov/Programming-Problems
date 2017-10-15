# https://www.hackerrank.com/challenges/ctci-linked-list-cycle

"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    fast = head
    slow = head
    while fast.next != None and fast.next.next != None:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True
    return False
        
    pass
