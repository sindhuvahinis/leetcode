class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        res = 0
        for count in counter.values():
            res += (count * (count - 1) // 2)
        return res