class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ms = {}
        mt = {}

        for i in range(len(s)):
            ms[s[i]] = ms.get(s[i], 0) + 1
            mt[t[i]] = mt.get(t[i], 0) + 1
        
        return ms == mt