class Solution:

    def DFS(self, grid, row, col, row0, col0):
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == 0:
            return

        grid[row][col] = 0
        self.shape.add((row - row0, col - col0))

        self.DFS(grid, row + 1, col, row0, col0)  # down
        self.DFS(grid, row - 1, col, row0, col0)  # up
        self.DFS(grid, row, col + 1, row0, col0)  # right
        self.DFS(grid, row, col - 1, row0, col0)  # left

    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        # calculate a code for each island
        self.shapes = set()

        nrows, ncols = len(grid), len(grid[0])
        for row in range(nrows):
            for col in range(ncols):
                self.shape = set()
                self.DFS(grid, row, col, row, col)

                if self.shape:
                    self.shapes.add(tuple(self.shape))

        return len(self.shapes)
