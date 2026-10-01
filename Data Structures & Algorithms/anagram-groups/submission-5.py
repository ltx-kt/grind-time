class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            cl = [0] * 26
            for c in s:
                cl[ord(c) - ord('a')] += 1
            d[tuple(cl)].append(s)
        return list(d.values())