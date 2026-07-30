class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set()
        for i in nums:
            s.add(i)

        res = 0
        # temp = 0
        for j in nums:
            if j-1 not in s:
                temp = 0
                while j + temp in s:
                    temp+=1
                res = max(temp, res)
        return res