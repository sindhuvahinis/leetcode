# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:

        self.res = 0
        map = collections.defaultdict(int)

        def dfs(root, csum):
            if not root:
                return

            csum += root.val

            if csum == sum:
                self.res += 1

            self.res += map[csum - sum]

            map[csum] += 1
            dfs(root.left, csum)
            dfs(root.right, csum)
            map[csum] -= 1

        dfs(root, 0)
        return self.res