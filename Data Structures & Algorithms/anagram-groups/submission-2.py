class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            idx = [0] * 26
            for char in s:
                idx[ord(char) - ord('a')] += 1
            if tuple(idx) not in d:
                d[tuple(idx)] = []
            d[tuple(idx)].append(s)
        return list(d.values())