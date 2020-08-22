class Solution:
    def maxArea(self, height: List[int]) -> int:

        n = len(height)
        l, r, Max = 0, n - 1, 0

        while l < r:
            area = min(height[l], height[r]) * (r - l)
            Max = max(Max, area)

            if height[l] > height[r]:
                r -= 1
            else:
                l += 1

        return Max