class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        _map = collections.defaultdict(list)

        for st in strs:
            sortSt = tuple(sorted(st))
            _map[sortSt].append(st)

        return list(_map.values())