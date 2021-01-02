# 1. Two Sum
# EASY

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        _map = {}

        for i, num in enumerate(nums):
            key = target - num

            if key in _map:
                return [_map[key], i]
            _map[num] = i

        return [-1, -1]