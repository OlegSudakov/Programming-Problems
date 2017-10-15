# https://www.hackerrank.com/challenges/insert-a-node-into-a-sorted-doubly-linked-list

"""
 Insert a node into a sorted doubly linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None, prev_node = None):
       self.data = data
       self.next = next_node
       self.prev = prev_node

 return the head node of the updated list 
"""
def SortedInsert(head, data):
    if head is None:
        return Node(data)
    if data < head.data:
        node = Node(data, next_node = head)
        head.prev = node
        return node
    curr_elem = head
    while curr_elem.next is not None:
        if curr_elem.data < data < curr_elem.next.data:
            new_node = Node(data, next_node = curr_elem.next, prev_node = curr_elem)
            curr_elem.next.prev = new_node
            curr_elem.next = new_node
            return head
        curr_elem = curr_elem.next
    new_node = Node(data, prev_node = curr_elem)
    curr_elem.next = new_node
    return head
