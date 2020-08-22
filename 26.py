class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        result = []

        if not matrix:
            return result

        m, n = len(matrix), len(matrix[0])

        rowBegin, rowEnd, colBegin, colEnd = 0, m - 1, 0, n - 1

        while rowBegin <= rowEnd and colBegin <= colEnd:

            for i in range(colBegin, colEnd + 1):
                result.append(matrix[rowBegin][i])

            rowBegin += 1

            for i in range(rowBegin, rowEnd + 1):
                result.append(matrix[i][colEnd])

            colEnd -= 1

            if rowBegin <= rowEnd:
                for i in range(colEnd, colBegin - 1, -1):
                    result.append(matrix[rowEnd][i])

            rowEnd -= 1

            if colBegin <= colEnd:
                for i in range(rowEnd, rowBegin - 1, -1):
                    result.append(matrix[i][colBegin])

            colBegin += 1

        return result