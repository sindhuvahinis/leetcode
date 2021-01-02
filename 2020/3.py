# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# There is a smart way to do it.
class Solution:
    def oddEvenList(self, head):

        if not head or not head.next:
            return head

        odd = head
        even = head.next
        curr = head.next

        while curr and curr.next:
            odd.next = curr.next
            odd = odd.next
            curr.next = odd.next
            odd.next = even

            curr = curr.next

        return head
