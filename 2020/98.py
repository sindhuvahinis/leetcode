class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # approach 1 : find the product of whole array and divide it with curr element

        # approach 2 : find the product of the left elements and array for product of right element.
        #            : product of left and right

        n = len(nums)

        left = [1] * n
        right = [1] * n

        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]

        res = [1] * n
        for i in range(0, n):
            res[i] = left[i] * right[i]

        return res