class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        start = 0
        longest = 0

        for i in range(len(s)):
            while s[i] in charSet:
                charSet.remove(s[start])
                start += 1
            charSet.add(s[i])
            longest = max(longest, i - start + 1)
            # print(longest)
        return longest