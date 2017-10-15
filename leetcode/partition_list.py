# https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head is None:
            return head
        slow_pointer = ListNode(0)
        slow_pointer_head = slow_pointer
        fast_pointer = head
        while fast_pointer is not None:
            if fast_pointer.val < x:
                slow_pointer.next = ListNode(fast_pointer.val)
                slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next
        fast_pointer = head
        while fast_pointer is not None:
            if fast_pointer.val >= x:
                slow_pointer.next = ListNode(fast_pointer.val)
                slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next
        return slow_pointer_head.next
