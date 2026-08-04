class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = {}
        start = 0
        longest = 0

        for i in range(len(s)):
            if s[i] in charSet:
                start = max(charSet[s[i]] + 1, start)
  
            charSet[s[i]] = i
            longest = max(longest, i - start + 1)
            # print(longest)
        return longest