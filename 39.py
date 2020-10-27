# 671. Second Minimum Node In a Binary Tree
# https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:

        if not root:
            return None

        def find(root, val):
            if not root:
                return float('inf')
            if root.val > val:
                return root.val
            return min(find(root.left, val), find(root.right, val))

        res = find(root, root.val)
        return -1 if res == float('inf') else res