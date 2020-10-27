# 366. Find Leaves of Binary Tree
# https://leetcode.com/problems/find-leaves-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        def remove_leaves(root, result, parent, isleft):
            if not root:
                return
            if not root.left and not root.right:
                result.append(root.val)
                if isleft:
                    parent.left = None
                elif parent:
                    parent.right = None

            remove_leaves(root.left, result, root, True)
            remove_leaves(root.right, result, root, False)

        result = []
        if not root:
            return result
        while root.left or root.right:
            ilist = []
            remove_leaves(root, ilist, None, False)
            result.append(ilist)
        result.append([root.val])

        return result