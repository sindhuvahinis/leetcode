# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:

    # time complexity : O(N^2) - going through entire list
    # space complexity : O(N)
    #     def DFS(self, preorder, inorder):
    #         if not inorder:
    #             return None

    #         rootval = preorder.popleft()
    #         rootindex = inorder.index(rootval)  # O(n)
    #         leftvalues = inorder[:rootindex]     #  O(n + k)
    #         rightvalues = inorder[rootindex+1:]  # O(n + k)

    #         root = TreeNode(rootval)

    #         root.left = self.DFS(preorder, leftvalues)
    #         root.right = self.DFS(preorder, rightvalues)

    #         return root

    # maintain a pre order index from 0 as root
    # index should point to the root element always

    # should maintain left and right index for inorder
    # list slicing boundaries

    # slice based on the index of the root element in preorder  # use index map
    # for left slicing (left, rootindex)
    # for right slicing (rootindex+1, right)

    # base condition if left > right

    def DFS(self, preorder, leftIndex, rightIndex):
        if leftIndex > rightIndex:
            return None

        rootval = preorder[self.preorderIndex]
        self.preorderIndex += 1
        root = TreeNode(rootval)

        rootIndex = self.indexmap[rootval]

        root.left = self.DFS(preorder, leftIndex, rootIndex - 1)
        root.right = self.DFS(preorder, rootIndex + 1, rightIndex)

        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        preorder = deque(preorder)
        self.preorderIndex = 0

        self.indexmap = {val: index for index, val in enumerate(inorder)}
        return self.DFS(preorder, 0, len(inorder) - 1)


