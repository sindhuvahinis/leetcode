# Problem 1 : Find whether given target exist in sorted array

def twoSum(nums, target):
    left, right = 0, len(nums)-1

    while left <= right:
        _sum = nums[left] + nums[right]

        if _sum == target:
            return True
        elif _sum < target:
            left += 1
        else:
            right -= 1

    return False

nums = [1, 2, 4, 5, 6]
print(twoSum(nums, 6))
print(twoSum(nums, 9))
print(twoSum(nums, 13))
