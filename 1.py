# Maximum product subarray
class Solution:
    def maxProduct(self, nums):

        Min, Max = nums[0], nums[0]

        result = Max

        for i in range(1, len(nums)):

            num = nums[i]
            if num < 0:
                # this is the key
                # negative number by default alternates the min and max.
                # we are reversing it to bring down that effect
                Min, Max = Max, Min

            Min = min(num, num * Min)
            Max = max(num, num * Max)
            result = max(result, Max)

        return result


s = Solution()
r = s.maxProduct([2, 3, -2, 4])
print(r)
