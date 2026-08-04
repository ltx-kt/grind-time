class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char = {}
        l = 0
        res = 0
        mf = 0
        for i in range(len(s)):
            char[s[i]] = char.get(s[i], 0) + 1
            mf = max(mf, char[s[i]])

            if (i - l + 1) - mf > k:
                char[s[l]] -= 1
                l += 1
            res = max(res, i - l + 1)
        return res
