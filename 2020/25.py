class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        result = set()
        dups = set()
        n = len(nums)

        for i in range(n - 2):

            Map = dict()
            if nums[i] not in dups:
                dups.add(nums[i])
                for j in range(i + 1, n):

                    value = -(nums[i] + nums[j])
                    if value in Map:
                        k = Map[value]
                        if k != i and k != j:
                            result.add(tuple(sorted((nums[i], nums[j], value))))

                    Map[nums[j]] = j

        return result