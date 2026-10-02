class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        hm = set()
        l = 0
        for r in range(len(s)):
            if s[r] in hm:
                while s[r] in hm:
                    hm.remove(s[l])
                    l += 1
            hm.add(s[r])
            res = max(res, r - l + 1)
        return res