from random import random


class Solution:
    def partition(self, res, left, right):

        pvIdx = random.randint(left, right)
        pivot = res[pvIdx]
        res[pvIdx], res[right] = res[right], res[pvIdx]

        for i in range(left, right):
            if res[i] < pivot:
                res[i], res[left] = res[left], res[i]
                left += 1

        res[left], res[right] = res[right], res[left]
        return left

    def quickSort(self, res, k):
        left = 0
        right = len(res) - 1

        while left < right:
            mid = self.partition(res, left, right)

            if mid == k:
                return
            elif mid < k:
                left = mid + 1
            else:
                right = mid - 1

    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        countMap = collections.Counter(words)
        res = [(-count, key) for key, count in countMap.items()]

        self.quickSort(res, k)
        res = res[:k]
        res.sort()

        return [key for _, key in res]