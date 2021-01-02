import collections


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

        banned = set(banned)
        normalized_str = ''

        for c in paragraph:
            if c.isalnum():
                normalized_str += c
            else:
                normalized_str += ' '

        _map = collections.defaultdict(int)
        maxCount = 0
        res = ''

        for word in normalized_str.split():
            word = word.lower()

            if word in banned:
                continue

            _map[word] += 1

            if maxCount < _map[word]:
                maxCount = _map[word]
                res = word

        return res