# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        if not head or not head.next:
            return None

        curr = prev = head

        for _ in range(n):
            curr = curr.next

        if not curr:
            return head.next

        while curr.next:
            prev = prev.next
            curr = curr.next

        prev.next = prev.next.next

        return head
