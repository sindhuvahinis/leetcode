"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def postorder(self, root: 'Node') -> List[int]:

        def DFS(root, res):
            if not root:
                return res

            for child in root.children:
                res = DFS(child, res)

            res.append(root.val)
            return res

        res = []
        DFS(root, res)
        return res