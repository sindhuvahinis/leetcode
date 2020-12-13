# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def dfs(self, root, target, length, K, res):
        if not root:
            return

        if root in self.parentmap:
            length = self.parentmap[root]

        if length == K:
            res.append(root.val)

        self.dfs(root.left, target, length + 1, K, res)
        self.dfs(root.right, target, length + 1, K, res)

    def find(self, root, target):
        if not root:
            return -1

        if root == target:
            self.parentmap[root] = 0
            return 0

        left = self.find(root.left, target)
        if left >= 0:
            self.parentmap[root] = left + 1
            return left + 1

        right = self.find(root.right, target)
        if right >= 0:
            self.parentmap[root] = right + 1
            return right + 1

        return -1

    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        self.parentmap = {}
        self.find(root, target)
        res = []
        self.dfs(root, target, self.parentmap[root], K, res)
        return res