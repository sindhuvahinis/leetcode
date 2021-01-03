# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def DFS(self, root1: TreeNode, root2: TreeNode, target: TreeNode) -> TreeNode:
        if root1:
            if root1 == target:
                self.ans = root2
            else:
                self.DFS(root1.left, root2.left, target)
                self.DFS(root1.right, root2.right, target)

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        self.DFS(original, cloned, target)
        return self.ans