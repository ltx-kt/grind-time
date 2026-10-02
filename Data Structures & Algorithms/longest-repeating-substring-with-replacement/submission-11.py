class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        hm = {}
        maxFreq = 0

        for r in range(len(s)):
            hm[s[r]] = hm.get(s[r], 0) + 1
            maxFreq = max(maxFreq, hm[s[r]])

            if (r - l + 1) - maxFreq > k:
                hm[s[l]] -= 1
                l += 1
            
            res = max(r - l + 1, res)
        
        return res