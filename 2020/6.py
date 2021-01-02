# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#validate BST
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def recur(root, lower=float('-inf'), upper=float('inf')):
            if not root:
                return True

            if root.val <= lower or root.val >= upper:
                return False

            return recur(root.left, lower, root.val) and recur(root.right, root.val, upper)

        return recur(root)