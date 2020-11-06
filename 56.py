class Solution:
    def maximumSwap(self, number: int) -> int:
        A = list(str(number))  # O(n)
        largemap = {int(num): i for i, num in enumerate(A)}

        for i, num in enumerate(A):
            for j in range(9, int(num), -1):
                if j in largemap and largemap[j] > i:
                    A[i], A[largemap[j]] = A[largemap[j]], A[i]
                    return int("".join(A))

        return number