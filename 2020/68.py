class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        start = 0
        n = len(A)

        res = 0

        for end in range(n):
            if A[end] == 0:
                K -= 1
                while K < 0:
                    if A[start] == 0:
                        K += 1
                    start += 1

            windowSize = end - start + 1
            res = max(res, windowSize)

        return res