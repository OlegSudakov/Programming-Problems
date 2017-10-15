# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        else:
            new_head =  self.__reverseList(head.next, head)
            head.next = None
            return new_head
        
    def __reverseList(self, head, prev):
        if head.next is None:
            head.next = prev
            return head
        else:
            new_head =  self.__reverseList(head.next, head)
            head.next = prev
            return new_head
