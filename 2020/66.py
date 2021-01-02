import heapq


class Solution:
    def _getCountOfLeftOfMid(self, matrix, mid):

        count = 0
        n = len(matrix)
        smallest = matrix[0][0]
        largest = matrix[n - 1][n - 1]

        row, col = n - 1, 0

        while row >= 0 and col < n:
            if matrix[row][col] <= mid:
                count += row + 1
                smallest = max(smallest, matrix[row][col])
                col += 1

            else:
                largest = min(largest, matrix[row][col])
                row -= 1

        return count, smallest, largest

    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        # Binary search technique

        # Base case
        if not len(matrix) or not len(matrix[0]):
            return None

        nrows = len(matrix)
        ncols = len(matrix[0])

        # range of number instead of indices
        # get start and end find the mid element

        start = matrix[0][0]
        end = matrix[nrows - 1][ncols - 1]

        while start < end:
            mid = start + (end - start) // 2

            # count no of elements left of mid
            count, smaller, larger = self._getCountOfLeftOfMid(matrix, mid)

            # if count == k , then return largest element which is SMALLER than mid
            if count == k:
                return smaller

            # if count < k then start = smallest element LARGER than mid
            elif count < k:
                start = larger

            # if count > k, then end = largest elt SMALLER than mid
            else:
                end = smaller

        return start

