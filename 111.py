class Solution:
    def trap(self, height: List[int]) -> int:

        # find the left max values
        # find the right max height values
        # curr water height = min(left, right) - currheight

        if not height:
            return 0

        n = len(height)
        left = [0] * n
        right = [0] * n

        left[0] = height[0]

        for index in range(1, n):
            left[index] = max(left[index - 1], height[index])

        right[n - 1] = height[n - 1]
        for index in range(n - 2, -1, -1):
            right[index] = max(right[index + 1], height[index])

        res = 0

        for index in range(0, n):
            res += min(left[index], right[index]) - height[index]

        return res

