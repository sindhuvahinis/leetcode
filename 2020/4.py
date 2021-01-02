"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

Copy with random pointer
"""


class Solution:
    visited = {}

    def copyRandomList(self, head: 'Node') -> 'Node':

        if not head:
            return head

        if head in self.visited:
            return self.visited[head]

        newNode = Node(head.val)
        self.visited[head] = newNode

        newNode.next = self.copyRandomList(head.next)
        newNode.random = self.copyRandomList(head.random)

        return newNode