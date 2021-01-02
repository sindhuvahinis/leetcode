# 21. Merge Two Sorted Lists
# EASY

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        res = ListNode(-1)
        curr = res

        l1h = l1
        l2h = l2

        while l1 and l2:
            if l1.val < l2.val:
                currval = l1
                l1 = l1.next
            else:
                currval = l2
                l2 = l2.next

            curr.next = currval
            curr = curr.next

        if l1:
            curr.next = l1
        elif l2:
            curr.next = l2

        return res.next