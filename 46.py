# https://leetcode.com/problems/shuffle-the-array/submissions/
# 1470. Shuffle the Array
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        lst=[]
        for i in range(n):
            lst+=[nums[i]]
            lst+=[nums[i+n]]
        return lst