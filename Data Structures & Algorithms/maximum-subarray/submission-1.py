class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float('-inf')
        sub = 0
        for r in range(len(nums)):
            sub = max(sub + nums[r], nums[r])
            res = max(res, sub)
        return res
