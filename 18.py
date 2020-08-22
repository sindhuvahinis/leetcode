class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        def recur(row, col, m, n):

            if row >= m or col >= n or row < 0 or col < 0:
                return 0

            if row == m - 1 and col == n - 1:
                return 1

            if dp[row][col] != -1:
                return dp[row][col]

            dp[row][col] = recur(row + 1, col, m, n) + recur(row, col + 1, m, n)
            return dp[row][col]

        dp = [[-1 for _ in range(n)] for _ in range(m)]
        return recur(0, 0, m, n)