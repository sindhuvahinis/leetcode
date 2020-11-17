from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:

        # BFS traversal
        # use map to couple the list

        queue = deque()
        queue.append((root, 0, 0))
        rmap = collections.defaultdict(list)

        min_x = max_x = 0
        while queue:
            tmp = collections.defaultdict(list)
            for i in range(len(queue)):
                node, x, y = queue.popleft();
                tmp[x].append(node.val)
                min_x = min(min_x, x)
                max_x = max(max_x, x)

                if node.left:
                    queue.append((node.left, x - 1, y - 1))

                if node.right:
                    queue.append((node.right, x + 1, y - 1))

            for i in tmp:
                rmap[i].extend(sorted(tmp[i]))

        res = []
        for key in range(min_x, max_x + 1):
            if key in rmap:
                res.append(rmap[key])

        return res