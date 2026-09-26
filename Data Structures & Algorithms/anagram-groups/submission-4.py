class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)
        for s in strs:
            c = [0] * 26
            for letter in s:
                c[ord(letter) - ord('a')] += 1
            hm[tuple(c)].append(s)
        return list(hm.values())