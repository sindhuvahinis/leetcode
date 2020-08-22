# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:

        if not head or not head.next:
            return head

        # find mid element

        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = None

        # print(head, slow)
        l1 = self.sortList(head)
        l2 = self.sortList(slow)

        return self.merge(l1, l2)

    def merge(self, l1, l2):
        mergeList = ListNode(0)
        curr = mergeList
        # print(l1, l2)
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = ListNode(l1.val)
                l1 = l1.next
                curr = curr.next
            else:
                curr.next = ListNode(l2.val)
                l2 = l2.next
                curr = curr.next

        if l1:
            curr.next = l1

        if l2:
            curr.next = l2

        return mergeList.next
