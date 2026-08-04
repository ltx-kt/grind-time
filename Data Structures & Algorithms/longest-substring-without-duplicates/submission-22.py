class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char = {}
        l = 0
        res = 0

        for i in range(len(s)):
            if s[i] in char:
                l = max(char[s[i]] + 1, l)
                char[s[i]] = i

            char[s[i]] = i
            res = max(res, i - l + 1)
        return res