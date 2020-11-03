# https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/
# 1026. Maximum Difference Between Node and Ancestor
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        if not root:
            return 0

        def dfs(root, cMax, cMin):
            if not root:
                return cMax - cMin

            cMax = max(cMax, root.val)
            cMin = min(cMin, root.val)
            left = dfs(root.left, cMax, cMin)
            right = dfs(root.right, cMax, cMin)

            return max(left, right)

        return dfs(root, root.val, root.val)