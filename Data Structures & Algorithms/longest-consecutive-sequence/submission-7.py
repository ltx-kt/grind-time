class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0

        s = set(nums)

        for i in s:
            if i - 1 in s:
                continue
            index = 0
            while i + index in s:
                index += 1
            res = max(res,index)
        return res