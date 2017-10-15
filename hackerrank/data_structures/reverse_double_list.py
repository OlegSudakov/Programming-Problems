# https://www.hackerrank.com/challenges/reverse-a-doubly-linked-list

"""
 Reverse a doubly linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None, prev_node = None):
       self.data = data
       self.next = next_node
       self.prev = prev_node

 return the head node of the updated list 
"""
def Reverse(head):
    if head is None or head.next is None:
        return head
    curr_elem = head
    while curr_elem.next is not None:
        true_next = curr_elem.next
        curr_elem.next = curr_elem.prev
        curr_elem.prev = true_next
        curr_elem = true_next
    curr_elem.next = curr_elem.prev
    curr_elem.prev = None
    return curr_elem
