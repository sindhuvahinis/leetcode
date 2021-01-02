# 515. Find Largest Value in Each Tree Row
# https://leetcode.com/problems/find-largest-value-in-each-tree-row/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:

        result = []
        if not root:
            return result

        queue = deque()
        queue.append(root)

        while queue:
            size = len(queue)
            Max = float('-inf')
            for _ in range(size):
                node = queue.popleft()
                Max = max(Max, node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(Max)

        return result

