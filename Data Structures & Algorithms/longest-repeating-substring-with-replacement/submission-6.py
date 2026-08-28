class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        freq = 0

        hm = {}
        res = 0


        for r in range(len(s)):
            hm[s[r]] = hm.get(s[r], 0) + 1
            freq = max(freq, hm[s[r]])

            if (r - l + 1) - freq > k:
                hm[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res
