# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        new_head = None
        head1 = l1
        head2 = l2
        if head1 is None and head2 is None:
            return None
        if head1 is None:
            return head2
        if head2 is None:
            return head1
        if head1.val <= head2.val:
            new_head = head1
            head1 = head1.next
        else:
            new_head = head2
            head2 = head2.next
        new_start = new_head
        while head1 and head2:
            if head1.val <= head2.val:
                new_head.next = head1
                new_head = new_head.next
                head1 = head1.next
            else:
                new_head.next = head2
                new_head = new_head.next
                head2 = head2.next
        if head1 is None:
            new_head.next = head2
        elif head2 is None:
            new_head.next = head1
        return new_start
