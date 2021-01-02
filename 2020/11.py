# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def helper(preorder, inorder):
            if not inorder:
                return None

            root = TreeNode(preorder.pop(0))
            index = inorder.index(root.val)
            left = inorder[0:index]
            right = inorder[index + 1:]
            root.left = helper(preorder, inorder[0:index])
            root.right = helper(preorder, inorder[index + 1:])

            return root

        return helper(preorder, inorder)