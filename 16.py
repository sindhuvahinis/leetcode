class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        sum_arr = [0] * n
        sum_arr[0] = nums[0]
        _max = nums[0]

        for i in range(1, n):
            sum_arr[i] = max(sum_arr[i - 1] + nums[i], nums[i])
            _max = max(sum_arr[i], _max)

        return _max