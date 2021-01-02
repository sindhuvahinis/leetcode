from collections import deque


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:

        # either DFS or BFS
        # will do BFS
        # queue add source pixel

        # Iterate through queue till its empty
        # 1. pop the node and change it's color to newcolor
        # 2. iterate through its neighbors and see if it is same color as source
        # 2a. if it is same color, add it to the queue
        # return the orginal image

        # Time complexity : O(N * M)
        # Space complexity : O (N * M)

        queue = deque()
        queue.append((sr, sc))

        directions = [
            [-1, 0],  # up
            [1, 0],  # down
            [0, -1],  # left
            [0, 1]  # right
        ]

        sourceColor = image[sr][sc]
        nrows = len(image)
        ncols = len(image[0])

        visited = set()
        visited.add((sr, sc))

        while queue:
            row, col = queue.popleft()
            image[row][col] = newColor
            for dir in directions:
                neighrow = row + dir[0]
                neighcol = col + dir[1]

                if neighrow < 0 or neighcol < 0 or neighrow >= nrows or neighcol >= ncols or (
                neighrow, neighcol) in visited:
                    continue

                visited.add((neighrow, neighcol))

                if image[neighrow][neighcol] == sourceColor:
                    queue.append((neighrow, neighcol))

        return image


