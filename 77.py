class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        countMap = collections.defaultdict(int)

        res = 0
        for t in time:
            if t % 60 == 0:
                res += countMap[0]
            else:
                res += countMap[60 - (t % 60)]
            countMap[t % 60] += 1

        return res