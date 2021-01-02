# 1570. Dot Product of Two Sparse Vectors
# https://leetcode.com/problems/dot-product-of-two-sparse-vectors/

class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = {}

        for index, num in enumerate(nums):
            self.nums[index] = num

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        prod = 0
        for index, num in self.nums.items():
            if index in vec.nums:
                prod += (vec.nums[index] * num)

        return prod

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)