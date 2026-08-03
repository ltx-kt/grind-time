class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        set1 = set()

        start = 0
        res = 0

        for i in range(len(s)):
            while s[i] in set1:
                set1.remove(s[start])
                start += 1
            set1.add(s[i])
            res = max(res, i - start + 1)
        return res