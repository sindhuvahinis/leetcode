class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        sum = 0
        for num in nums:
            sum += num
            res.append(sum)

        return res