# https://leetcode.com/problems/diameter-of-binary-tree/
# 543. Diameter of Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 0

        def depth(root):
            if not root:
                return 0
            L = depth(root.left)
            R = depth(root.right)
            self.ans = max(self.ans, L + R)
            return max(L, R) + 1

        depth(root)
        return self.ans

