class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s1 = {}
        start = 0
        length = 0
        temp = 0
        for i in range(len(s)):
            if s[i]  in s1:
                while start < s1[s[i]]:
                    start +=1
                    temp -= 1
            s1[s[i]] = i + 1
            temp +=1
            length = max(length, temp)
            # print(length)
        return length
    
