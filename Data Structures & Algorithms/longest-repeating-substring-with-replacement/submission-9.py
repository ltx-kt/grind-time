class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        res = 0
        maxfreq = 0
        hm = {}
        l = 0
        for r in range(len(s)):
            hm[s[r]] = hm.get(s[r], 0) + 1
            maxfreq = max(maxfreq, hm[s[r]])

            if (r - l + 1) - maxfreq > k:
                hm[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res

