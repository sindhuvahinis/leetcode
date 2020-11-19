# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return ""

        queue = deque()
        queue.append(root)
        res = []
        res.append(str(root.val))

        while queue:
            size = len(queue)

            for i in range(size):
                node = queue.popleft()

                res.append(',')
                if node.left:
                    res.append(str(node.left.val))
                    queue.append(node.left)
                else:
                    res.append('#')

                res.append(',')

                if node.right:
                    res.append(str(node.right.val))
                    queue.append(node.right)
                else:
                    res.append('#')

        print(''.join(res))
        return ''.join(res)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """

        if not data:
            return None

        seq = data.split(',')
        parent = None
        root = TreeNode(int(seq[0]))
        queue = deque()
        queue.append(root)

        i = 1
        while i < len(seq):
            node = queue.popleft()

            if seq[i] != '#':
                node.left = TreeNode(int(seq[i]))
                queue.append(node.left)
            i += 1

            if seq[i] != '#':
                node.right = TreeNode(int(seq[i]))
                queue.append(node.right)
            i += 1

        return root

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans