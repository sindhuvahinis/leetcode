class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = _sum = 0
        _map = {}
        n = len(nums)
        _map[0] = 1
        for i in range(n):
            _sum += nums[i]
            if _sum - k in _map:
                count += _map[_sum - k]
            _map[_sum] = _map.get(_sum, 0) + 1

        return count