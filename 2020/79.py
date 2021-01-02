# 572. SubTree of another Tree
# EASY

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isSubTreeForNode(self, root, subTree):
        if not root and not subTree:
            return True

        elif not root or not subTree:
            return False
        else:
            return root.val == subTree.val and self.isSubTreeForNode(root.left, subTree.left) and self.isSubTreeForNode(
                root.right, subTree.right)

    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s:
            return False

        return self.isSubTreeForNode(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
