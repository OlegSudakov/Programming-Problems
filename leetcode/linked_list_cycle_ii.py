# https://leetcode.com/problems/linked-list-cycle-ii/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pointer = head
        visited = set()
        beginning = None
        while head:
            if head in visited:
                beginning = head
                break
            else:
                visited.add(head)
            head = head.next
        return beginning
