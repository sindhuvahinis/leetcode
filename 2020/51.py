# https://leetcode.com/problems/interval-list-intersections/
# 986. Interval List Intersections
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:

        i, j = 0, 0
        A.sort(key=lambda x: x[0])
        B.sort(key=lambda x: x[0])

        res = []

        while i < len(A) and j < len(B):

            start = max(A[i][0], B[j][0])
            end = min(A[i][1], B[j][1])

            if start <= end:
                res.append((start, end))

            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1

        return res