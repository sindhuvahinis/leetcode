# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:

        result = []

        if not root:
            return result

        # Traversal - BFS
        # reverse the list for every alternative level
        # append it to the list

        queue = deque()
        queue.append(root)

        # flag to reverse the level list
        isReverse = False

        while queue:
            size = len(queue)

            level = deque()

            for _ in range(size):
                node = queue.popleft()
                if isReverse:
                    level.appendleft(node.val)
                else:
                    level.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            # inverting the flag value as we need to reverse for alternative level
            isReverse = not isReverse
            result.append(level)

        return result