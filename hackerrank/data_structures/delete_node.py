# https://www.hackerrank.com/challenges/delete-a-node-from-a-linked-list

"""
 Delete Node at a given position in a linked list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method. 
"""

def Delete(head, position):
    if head is None:
        return head
    if position == 0:
        t = head
        head = head.next
        del t
        return head
    cur = head
    for i in range(position-1):
        cur = cur.next
        if cur is None:
            return head
    if not cur.next.next is None:
        t = cur.next
        cur.next = cur.next.next
        del t
    else:
        t = cur.next
        cur.next = None
        del t
    return head
