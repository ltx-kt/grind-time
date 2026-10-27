class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        
        maxF = 0

        hm = {}
        for r in range(len(s)):
            hm[s[r]] = hm.get(s[r], 0) + 1
            maxF = max(maxF, hm[s[r]])

            if (r - l + 1) - maxF > k:
                hm[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        return res