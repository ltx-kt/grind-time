class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in strs:
            code = [0] * 26
            for c in i:
                code[ord(c) - ord('a')] += 1
            if tuple(code) not in d:
                d[tuple(code)] = []
            d[tuple(code)].append(i)
        return list(d.values())
