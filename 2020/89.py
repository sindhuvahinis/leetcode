# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        self.res = 0

        def helper(root):
            if not root:
                return [0, 0.0]

            count1, sum1 = helper(root.left)
            count2, sum2 = helper(root.right)

            count = count1 + count2 + 1
            _sum = sum1 + sum2 + root.val

            self.res = max(self.res, _sum / count)
            return [count, _sum]

        helper(root)
        return self.res