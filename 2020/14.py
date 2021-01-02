class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def binarySearch(nums, target, isfirst):

            start, end = 0, len(nums) - 1

            index = -1

            while start <= end:

                mid = start + (end - start) // 2


                if nums[mid] == target:
                    index = mid
                    if isfirst:
                        end = mid - 1
                    else:
                        start = mid + 1
                elif nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1

            return index

        fI = binarySearch(nums, target, True)
        lI = binarySearch(nums, target, False)

        return [fI, lI]