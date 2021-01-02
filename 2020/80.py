# 994. Rotten Tomatoes
# MEDIUM

from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        # first traverse and insert the rotten tomatoes into queue

        # maintain a time to keep track the the time

        # add minute and row and col in queue
        # while queue is not empty
        # pick each cell from queue
        #  1. makes its adjacents as rotten (if it is fresh orange)
        #  2. insert the new rotten into queue

        nrows = len(grid)
        ncols = len(grid[0])

        queue = deque()

        for row in range(nrows):
            for col in range(ncols):
                if grid[row][col] == 2:
                    queue.append((row, col, 0))

        dirs = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        maxtime = 0
        while queue:
            row, col, time = queue.popleft()
            maxtime = max(time, maxtime)

            for dir in dirs:
                newrow = row + dir[0]
                newcol = col + dir[1]

                if newrow < 0 or newcol < 0 or newrow >= nrows or newcol >= ncols:
                    continue

                if grid[newrow][newcol] == 1:
                    grid[newrow][newcol] = 2
                    queue.append((newrow, newcol, time + 1))

        for row in range(nrows):
            for col in range(ncols):
                if grid[row][col] == 1:
                    return -1

        return maxtime