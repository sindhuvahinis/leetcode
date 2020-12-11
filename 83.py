class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        # if the current element in matrix is 1,
        #   1. check its neighbour elements and check if its 1 or greater
        #   2. min of the neighbour elements and add 1

        nrows = len(matrix)
        ncols = len(matrix[0])

        dp = [[0] * (ncols + 1) for _ in range((nrows + 1))]

        maxlen = 0
        for i in range(1, nrows + 1):
            for j in range(1, ncols + 1):
                if matrix[i - 1][j - 1] == '1':
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1
                    maxlen = max(maxlen, dp[i][j])

        return maxlen * maxlen