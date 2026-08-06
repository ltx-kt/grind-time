class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        # cd = {}

        l = 0
        # for r in range(len(s)):
        #     if s[r] in cd:
        #         # cd[l]
        #         l = max(r - cd[s[l]] + 1, l)
        #     cd[s[r]] = r
        #     res = max(res, r - l + 1)
        # return res
        cd = set()
        for r in range(len(s)):
            while s[r] in cd:
                cd.remove(s[l])
                l += 1
            cd.add(s[r])
         
            res = max(res, r - l + 1)
        return res