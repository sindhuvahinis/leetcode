class Solution:
    def partitionLabels(self, S: str) -> List[int]:

        _map = {c: i for i, c in enumerate(S)}

        _max = prevIndex = 0
        res = []

        for i, c in enumerate(S):
            _max = max(_max, _map[c])

            if _max == i:
                res.append(i - prevIndex + 1)
                prevIndex = i + 1

        return res