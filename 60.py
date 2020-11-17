import collections

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = maxlen = 0
        _map = collections.defaultdict(int)

        for end in range(len(s)):
            c = s[end]

            while c in _map:
                _map[s[start]] -= 1

                if _map[s[start]] == 0:
                    del (_map[s[start]])

                start += 1

            _map[s[end]] += 1
            maxlen = max(maxlen, end - start + 1)

        return maxlen