class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss = {}
        tt = {}
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            ss[s[i]] = ss.get(s[i], 0) + 1
            tt[t[i]] = tt.get(t[i], 0) + 1
        
        return ss == tt
        