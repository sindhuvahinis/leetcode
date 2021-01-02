# https://leetcode.com/problems/same-tree/
# 100. Same Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # iterate through each and every node in p and q
        if (p and not q) or (not p and q):
            return False
        if not p and not q:
            return True

        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)