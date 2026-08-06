class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        maxFreq = 0
        cd = {}
        l = 0

        for r in range(len(s)):
            cd[s[r]] = cd.get(s[r], 0) + 1
            maxFreq = max(maxFreq, cd[s[r]])

            if (r - l + 1) - maxFreq > k:
                cd[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res