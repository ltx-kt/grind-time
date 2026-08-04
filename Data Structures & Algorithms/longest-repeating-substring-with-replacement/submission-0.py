class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        c = {}
        l = 0
        res = 0

        for i in range(len(s)):
            c[s[i]] = c.get(s[i], 0) + 1

            while (i - l + 1) - max(c.values()) > k:
                c[s[l]] -= 1
                l += 1
            res = max(res, i - l + 1)        
        return res