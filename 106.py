# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        # 100 + 900 = 1000
        # 001 + 009 = 0001

        # add each node in l1 and l2 respectively
        # sum % 10 add it to the result
        # sum // 10 - carry bit

        # sum = l1.val + l2.val + carry

        # loop through l1 and l2 separately and add the prev carry bit

        carry = 0
        res = ListNode(-1)
        curr = res

        while l1 or l2:

            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            sum = val1 + val2 + carry
            curr.next = ListNode(sum % 10)
            curr = curr.next

            carry = sum // 10

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        if carry:
            curr.next = ListNode(carry)

        return res.next