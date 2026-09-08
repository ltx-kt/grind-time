class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l = 0
        res = float('-inf')
        sub = 0
        for r in range(len(nums)):
            if sub < 0:
                l = r
                sub = 0
            sub += nums[r]
            res = max(res, sub)
        return res
