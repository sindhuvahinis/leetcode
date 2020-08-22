class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        n = len(nums)
        start, end = 0, n - 1

        while start <= end:
            mid = start + (end - start) // 2

            left, right = mid - 1, mid + 1

            leftVal = float('-inf') if left < 0 else nums[left]
            rightVal = float('-inf') if right >= n else nums[right]

            if leftVal < nums[mid] and rightVal < nums[mid]:
                return mid
            elif leftVal > nums[mid]:
                end = left
            else:
                start = right

        return -1